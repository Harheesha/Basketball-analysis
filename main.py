from utils.video_utils import read_video, save_video
from tracker.player_tracker import PlayerTracker
from tracker.ball_tracker import BallTracker
from drawer import PlayerTracksDrawer
from drawer import BallTracksDrawer
from drawer import TeamBallControlDrawer
from drawer import PassInterceptionDrawer
from drawer import CourtKeypointDrawer
from drawer import TacticalViewDrawer
from team_assigner import TeamAssigner
from pass_and_interception_detector import PassAndInterceptionDetector
from ball_aquisition import BallAquisitionDetector
from court_keypoint_detector import CourtKeypointDetector
from tactical_view_converter.tactical_view_converter import TacticalViewConverter


def main():
    video_frames = read_video(
        "/content/drive/MyDrive/Basketball analysis /input video/video_2.mp4"
    )

    player_tracker = PlayerTracker(
        "/content/drive/MyDrive/Basketball analysis /models/player_detector.pt"
    )
    ball_tracker = BallTracker(
        "/content/drive/MyDrive/Basketball analysis /models/ball_detector.pt"
    )
    court_keypoint_detector = CourtKeypointDetector(
        "/content/drive/MyDrive/Basketball analysis /models/court_keypoint_detector.pt"
    )
    court_keypoint_drawer = CourtKeypointDrawer()

    court_keypoints_per_frame = court_keypoint_detector.get_court_keypoints(
        video_frames,
        read_from_stub=True,
        stub_path="/content/drive/MyDrive/Basketball analysis /stubs/court_key_points_stub.pkl",
    )

    player_tracks = player_tracker.get_object_tracks(
        video_frames,
        read_from_stub=True,
        stub_path="/content/drive/MyDrive/Basketball analysis /tracker/_playertrack_stubs.pkl",
    )
    ball_tracks = ball_tracker.get_object_tracks(
        video_frames,
        read_from_stub=True,
        stub_path="/content/drive/MyDrive/Basketball analysis /tracker/ball_tracks_stubs.pkl",
    )
    ball_tracks = ball_tracker.remove_wrong_detections(ball_tracks)
    ball_tracks = ball_tracker.interpolate_ball_positions(ball_tracks)

    player_track_drawer = PlayerTracksDrawer()
    ball_tracks_drawer = BallTracksDrawer()

    team_assigner = TeamAssigner()
    player_assignment = team_assigner.get_player_teams_across_frames(
        video_frames,
        player_tracks,
        read_from_stub=True,
        stub_path="/content/drive/MyDrive/Basketball analysis /tracker/team_assigner_stubs.pkl",
    )

    ball_aquisition_detector = BallAquisitionDetector()
    ball_aquisition = ball_aquisition_detector.detect_ball_possession(
        player_tracks, ball_tracks
    )

    team_ball_control_drawer = TeamBallControlDrawer()

    pass_and_interception_detector = PassAndInterceptionDetector()
    passes = pass_and_interception_detector.detect_passes(
        ball_aquisition, player_assignment
    )
    interceptions = pass_and_interception_detector.detect_interceptions(
        ball_aquisition, player_assignment
    )
    pass_and_interceptions_drawer = PassInterceptionDrawer()

    tactical_view_converter = TacticalViewConverter(
        court_image_path="./images/basketball_court.png"
    )
    tactical_player_positions = tactical_view_converter.transform_players_to_tactical_view(
        court_keypoints_per_frame, player_tracks
    )
    tactical_view_drawer = TacticalViewDrawer()


    # Draw overlays
    output_video_frames = player_track_drawer.draw(
        video_frames,
        player_tracks,
        player_assignment,
        ball_aquisition,
    )
    output_video_frames = ball_tracks_drawer.draw(output_video_frames, ball_tracks)
    output_video_frames = team_ball_control_drawer.draw(
        output_video_frames,
        player_assignment,
        ball_aquisition,
    )
    output_video_frames = pass_and_interceptions_drawer.draw(
        output_video_frames,
        passes,
        interceptions,
    )
    output_video_frames = court_keypoint_drawer.draw(
        output_video_frames,
        court_keypoints_per_frame,
    )

    output_video_frames = tactical_view_drawer.draw(output_video_frames,
                                                    tactical_view_converter.court_image_path,
                                                    tactical_view_converter.width,
                                                    tactical_view_converter.height,
                                                    tactical_view_converter.key_points,
                                                    tactical_player_positions,
                                                    player_assignment,
                                                    ball_aquisition,
                                                    )
    save_video(
        output_video_frames,
        "/content/drive/MyDrive/Basketball analysis /output video/video_1.avi",
    )


if __name__ == "__main__":
    main()
