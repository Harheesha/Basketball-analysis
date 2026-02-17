# 🏀 Basketball Analysis with Computer Vision
This project analyzes basketball game videos using computer vision. It detects and tracks players and the ball, assigns teams based on jersey appearance, estimates ball possession and passes, and visualizes player positions on a top‑down court view. [web:229][web:286]

---

## Demo

Download or play the demo video directly from this repository:

- [Demo video](./demo.gif)

## Features

- Player and ball detection with YOLO models. [web:229]
- Multi-object tracking to keep consistent player IDs across frames.
- Team assignment using jersey appearance (CLIP / Fashion-CLIP). [web:229]
- Ball possession, passes, and interceptions estimated from trajectories. [web:229]
- Court keypoint detection and homography to map broadcast view to a standard court. [web:229]
- Tactical top‑down view rendered from player and ball positions. [web:229]

## Project Structure

```bash
Basketball-analysis/
├── main.py
├── models/                         # Model weights (not tracked in git)
├── input video/                    # Input game clips
├── output video/                   # Generated analysis videos
├── utils/
├── tracker/
├── drawer/
├── team_assigner/
├── ball_aquisition/
├── pass_and_interception_detector/
├── court_keypoint_detector/
├── tactical_view_converter/
├── images/
└── requirements.txt
```


---

## Model Weights

Model weights are not stored in this repository due to size limitations.

Download the trained weights:

- **Ball Detector**  
  https://drive.google.com/file/d/1erVj2_IvLnrUETt3bmNg57NJ8H3BthhF/view?usp=drive_link  

- **Player Detector**  
  https://drive.google.com/file/d/13Dp9han66kl0GjM18vH7otpr9rLnK7Dr/view?usp=drive_link  

- **Court Keypoint Detector**  
  https://drive.google.com/file/d/1xt9kCNdScXv29YpWWAnz1dOOXFIXdF3W/view?usp=drive_link  

After downloading, place all weights inside the `models/` directory before running the project.

---

## Installation and Usage (Local)

### 1. Clone the Repository

Installation and Usage (Local)
1. Clone the Repository
```python
git clone https://github.com/Harheesha/Basketball-analysis.git
cd Basketball-analysis
```
### 2. Install Dependencies
```python
pip install -r requirements.txt
```
### 3. Add Input Video

Place your video inside:

input video/


Example:

[input video](./video_2.mp4)

Make sure `main.py` points to the correct input video path.

### 4. Run the Project

```python
python main.py
```

The analyzed video will be saved inside:

output video/


Example output:

[output video](./video_1.avi)

---

## Running on Google Colab

### 1. Mount Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
```

2. Clone Repository
```python
!git clone https://github.com/Harheesha/Basketball-analysis.git
%cd Basketball-analysis
```

3. Copy Model Weights from Drive
```python
!cp -r "/content/drive/MyDrive/Basketball analysis/models" "/content/Basketball-analysis/models"
```

4. Install Dependencies
```python
!pip install -r requirements.txt
```
5. Run the Pipeline
```python
!python main.py
```
Download the resulting video from the [output video/] directory.

---

Future Work

-Improve tracking under heavy occlusion

-Detect additional events (shots, rebounds, screens)

-Add a simple web UI for uploading and viewing analysis results

---

Requirements

All dependencies are listed in:
```python
requirements.txt
```

Install them with:
```python
pip install -r requirements.txt
```
