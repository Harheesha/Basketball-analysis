# Basketball Analysis with Computer Vision

Real-time basketball game analysis using computer vision for player tracking, team assignment, ball possession detection, and tactical visualization.

**Demo:** [Download Demo Video](demo.gif)

---

## Overview

This system analyzes basketball game footage to extract tactical and statistical insights. It combines multiple computer vision models to detect players and the ball, track their movements across frames, assign team affiliations, estimate ball possession and passing sequences, and generate a top-down tactical view of the game.

**Key capabilities:**
- Player and ball detection using YOLO models
- Multi-object tracking with consistent player IDs
- Team assignment via jersey appearance analysis (CLIP/Fashion-CLIP)
- Ball possession, pass, and interception detection from trajectories
- Court keypoint detection and homography mapping
- Tactical top-down view generation from broadcast footage

---

## Technical Architecture

### Models Used

| Component | Model | Purpose |
|-----------|-------|---------|
| Player Detection | YOLOv11 | Detect all players on court |
| Ball Detection | YOLOv8 | Track basketball across frames |
| Team Assignment | Fashion-CLIP | Jersey-based team classification |
| Court Mapping | Custom CNN | Keypoint detection for homography |

### Pipeline

```
Input Video → Frame Processing → Detection (YOLO) → Tracking → 
Team Assignment → Ball Possession → Court Mapping → 
Tactical View Generation → Output Video
```

Each frame is processed through:
1. **Detection:** YOLO models identify players and ball
2. **Tracking:** Multi-object tracker maintains consistent IDs
3. **Team Classification:** Jersey analysis assigns players to teams
4. **Possession Analysis:** Ball trajectory determines possession and passes
5. **Court Projection:** Homography transforms broadcast view to tactical top-down view
6. **Rendering:** Annotated broadcast view + tactical overlay

---

## Project Structure

```
Basketball-analysis/
├── main.py                           # Main pipeline
├── models/                           # Model weights (download separately)
├── input_video/                      # Input game footage
├── output_video/                     # Generated analysis
├── utils/                            # Helper functions
├── tracker/                          # Multi-object tracking
├── drawer/                           # Visualization utilities
├── team_assigner/                    # Team classification
├── ball_acquisition/                 # Possession detection
├── pass_and_interception_detector/   # Pass analysis
├── court_keypoint_detector/          # Court mapping
├── tactical_view_converter/          # Top-down view generation
├── images/                           # Assets
├── requirements.txt                  # Dependencies
└── README.md
```

---

## Installation

### Prerequisites

- Python 3.8+
- CUDA-capable GPU (recommended for real-time processing)
- 8GB+ RAM

### Setup

1. **Clone repository**

```bash
git clone https://github.com/Harheesha/Basketball-analysis.git
cd Basketball-analysis
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Download model weights**

Due to file size constraints, model weights are hosted separately:

- [Ball Detector](https://drive.google.com/file/d/1erVj2_IvLnrUETt3bmNg57NJ8H3BthhF/view?usp=drive_link) (YOLOv8)
- [Player Detector](https://drive.google.com/file/d/13Dp9han66kl0GjM18vH7otpr9rLnK7Dr/view?usp=drive_link) (YOLOv11)
- [Court Keypoint Detector](https://drive.google.com/file/d/1xt9kCNdScXv29YpWWAnz1dOOXFIXdF3W/view?usp=drive_link)

Place all weights in the `models/` directory:

```bash
models/
├── ball_detector.pt
├── player_detector.pt
└── court_keypoints.pt
```

4. **Add input video**

Place your basketball game video in `input_video/`:

```bash
input_video/
└── your_game.mp4
```

Update the video path in `main.py` if needed.

---

## Usage

### Local Execution

```bash
python main.py
```

Output will be saved to `output_video/`.

### Configuration

Edit `main.py` to adjust:
- Input/output paths
- Detection confidence thresholds
- Tracking parameters
- Visualization options

### Google Colab

For cloud execution:

1. **Mount Drive**

```python
from google.colab import drive
drive.mount('/content/drive')
```

2. **Clone and setup**

```python
!git clone https://github.com/Harheesha/Basketball-analysis.git
%cd Basketball-analysis
```

3. **Copy models from Drive**

```python
!cp -r "/content/drive/MyDrive/Basketball analysis/models" "/content/Basketball-analysis/models"
```

4. **Install and run**

```python
!pip install -r requirements.txt
!python main.py
```

Download results from `output_video/`.

---

## Output

The system generates:

1. **Annotated broadcast view** with:
   - Player bounding boxes and IDs
   - Team colors
   - Ball tracking
   - Possession indicators
   - Pass annotations

2. **Tactical top-down view** showing:
   - Player positions on standard court
   - Ball location
   - Movement trajectories
   - Team formations

---

## Performance

Tested on NVIDIA RTX 3060:
- **Processing speed:** ~15-20 FPS (1080p input)
- **Detection accuracy:** Player ~92%, Ball ~87%
- **Tracking consistency:** ~90% ID retention across occlusions

CPU-only processing: ~3-5 FPS

---

## Dependencies

Core libraries (see `requirements.txt` for versions):

- `ultralytics` - YOLO models
- `opencv-python` - Video processing
- `torch`, `torchvision` - Deep learning backend
- `numpy`, `pandas` - Data processing
- `supervision` - Tracking utilities
- `transformers` - CLIP models
- `pillow` - Image operations

Install all:

```bash
pip install -r requirements.txt
```

---

## Current Limitations

- Tracking degrades under heavy player occlusion (>3 seconds)
- Team assignment may fail in poor lighting or similar jersey colors
- Court keypoint detection requires clear court markings
- Processing speed depends heavily on hardware

---

## Future Improvements

- [ ] Improve tracking robustness with trajectory prediction
- [ ] Add shot detection and classification (layups, 3-pointers, etc.)
- [ ] Detect rebounds, screens, and defensive actions
- [ ] Support for multi-camera inputs
- [ ] Web interface for video upload and analysis
- [ ] Real-time streaming support
- [ ] Model optimization for edge deployment

---

## Technical Details

### Detection

YOLO models run at 640x640 input resolution with:
- Confidence threshold: 0.5
- NMS threshold: 0.4
- Detection classes: Person (players), Sports ball (basketball)

### Tracking

Uses ByteTrack algorithm with:
- Track threshold: 0.6
- Match threshold: 0.8
- Track buffer: 30 frames

### Team Assignment

Fashion-CLIP analyzes cropped player regions:
- Extracts dominant jersey color
- Clusters into two teams using appearance similarity
- Updates assignments across frames for consistency

### Court Mapping

Detects court keypoints (corners, three-point line, etc.) to compute homography matrix:
- Maps broadcast pixel coordinates to standard court coordinates
- Enables top-down tactical view generation
- Handles different camera angles and zoom levels

---

## Contributing

Contributions welcome. Please:
1. Fork the repository
2. Create a feature branch
3. Make changes with clear commit messages
4. Submit a pull request

Areas for contribution:
- Tracking improvements under occlusion
- Additional event detection (shots, rebounds)
- Performance optimization
- Documentation

---

## License

MIT License - see LICENSE file for details.

---

## Citation

If you use this work in research, please cite:

```bibtex
@software{basketball_analysis_2024,
  author = {Adebanjo, Aishat},
  title = {Basketball Analysis with Computer Vision},
  year = {2024},
  url = {https://github.com/Harheesha/Basketball-analysis}
}
```

---

## Contact

**Aishat Adebanjo**  
Email: aishatadebanjo34@gmail.com  
LinkedIn: [linkedin.com/in/adebanjo-aishat](https://linkedin.com/in/adebanjo-aishat)  
GitHub: [@Harheesha](https://github.com/Harheesha)

---

## Acknowledgments

- Ultralytics for YOLO implementations
- OpenAI for CLIP model
- ByteTrack for tracking algorithm

---

**Built by Aishat Adebanjo | Machine Learning Engineer specializing in Computer Vision**
