import cv2
import os
import pickle

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def save_video(output_video_frame, output_video_path):
    if not os.path.exists(os.path.dirname(output_video_path)):
        os.makedirs(os.path.dirname(output_video_path))

    h, w = output_video_frame[0].shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24.0, (w, h))

    for frame in output_video_frame:
        out.write(frame)
    out.release()

def read_stub(read_from_stub, stub_path):
    if not read_from_stub or stub_path is None or not os.path.exists(stub_path):
        return None
    with open(stub_path, "rb") as f:
        return pickle.load(f)

def save_stub(stub_path, tracks):
    if stub_path is None:
        return
    with open(stub_path, "wb") as f:
        pickle.dump(tracks, f)
