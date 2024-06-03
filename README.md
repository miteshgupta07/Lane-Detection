<div align="center">
<h1> 🛣️🚗 Lane Detection 🚗🛣️ </h1>
</div>
This project implements lane detection on video streams using OpenCV and Python. The lanes are detected using edge detection and Hough Line Transform, and the detected lanes are highlighted and filled with color in the output video.

## Features

- Convert image frames to grayscale and apply Gaussian blur
- Perform Canny edge detection
- Define a region of interest to focus on the road area
- Detect lines using Hough Line Transform
- Average the detected lines to get a single left and right lane line
- Fill the lane area with a specified color


<img width="852" alt="image" src="https://github.com/miteshgupta07/Lane-Detection-Using-Computer-Vision/assets/111682782/11f05f8e-aca9-48d3-98d0-e71d8f5c0987">



## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/miteshgupta07/lane-detection.git
    ```
2. Navigate to the project directory:
    ```sh
    cd lane-detection
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your video file (e.g., `test2.mp4`) in the project directory.
2. Run the main script:
    ```sh
    python main.py
    ```
3. The processed video with detected and filled lanes will be displayed.
