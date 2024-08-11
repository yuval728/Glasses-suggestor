# Glasses Overlay Application

This application uses OpenCV to overlay glasses images on detected faces in real-time from a webcam feed. The user can cycle through different glasses images using keyboard inputs.

## Requirements

- Python 3.x
- OpenCV
- A directory named `Glasses` containing images of glasses with transparent backgrounds (PNG format recommended)

## Installation

1. Install Python 3.x from [python.org](https://www.python.org/).
2. Install OpenCV using pip:
    ```sh
    pip install opencv-python
    ```

## Usage

1. Ensure you have a directory named `Glasses` in the same directory as the script. This directory should contain images of glasses.
2. Run the script:
    ```sh
    python script_name.py
    ```
3. Use the following keys to interact with the application:
    - `d`: Move to the next glasses image.
    - `a`: Move to the previous glasses image.
    - `r`: Reset to the first glasses image.
    - `q`: Quit the application.

## How It Works

1. The script lists all images in the `Glasses` directory.
2. It captures video from the webcam.
3. It uses a pre-trained Haar Cascade classifier to detect faces in the video feed.
4. It overlays the selected glasses image on the detected faces.
5. The user can cycle through the glasses images using the keyboard.

## Example

Place your glasses images in the `Glasses` directory like this:
Glasses/ ├── glasses1.png ├── glasses2.png ├── glasses3.png ...

Run the script and see the glasses overlay on your face in real-time!