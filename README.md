# Detecting Color

This project demonstrates real-time color detection using OpenCV and Python. It uses a webcam feed to detect objects of a specific color (e.g., red) and highlights them with bounding rectangles.

## Features

- Detects objects of a specific color in real-time.
- Supports color detection across hue boundaries (e.g., red at hue 0 and 180).
- Displays the video feed with detected objects highlighted.
- Adjustable parameters for filtering small objects.

## Requirements

- Python 3.10 or later
- OpenCV (`cv2`)
- NumPy (`numpy`)

## Installation

1. Clone the repository:
   ```powershell
   git clone https://github.com/your-username/detecting-color.git
   cd detecting-color
   ```

2. Install the required Python packages:
   ```powershell
   pip install opencv-python numpy
   ```

## Usage

1. Run the `main.py` script:
   ```powershell
   python main.py
   ```

2. The webcam feed will open, and objects of the specified color (default: red) will be detected and highlighted.

3. Press `q` to exit the application.

## How It Works

- The `util.py` file contains the `get_limits` function, which calculates HSV ranges for a given BGR color.
- The `main.py` file uses OpenCV to process the webcam feed, apply color masks, and detect contours of objects matching the specified color.

## Customization

- To detect a different color, modify the `red` variable in `main.py` to the desired BGR color.
- Adjust the `area` threshold in `main.py` to filter out smaller objects.

