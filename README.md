# YOLO Object Detection with Streamlit

This project is a Streamlit-based web application for real-time object detection using the YOLO model. It uses a webcam feed to detect and classify objects as "Ripe" or "Unripe" with bounding boxes displayed on the live video feed.

## Features

- **Real-Time Detection**: Uses a webcam feed for live object detection.
- **YOLO Integration**: Leverages the YOLO model for accurate object detection and classification.
- **Streamlit Interface**: Provides an interactive GUI for ease of use.

## Requirements

The project requires the following dependencies:

- `streamlit`
- `opencv-python`
- `opencv-contrib-python`
- `cvzone`
- `ultralytics`

Ensure you have Python 3.8 or later installed.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Place the YOLO model weights (best.pt) in the same directory as the script or adjust the path in the code.

## Usage

1. Run the streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open the app in your web browser at http://localhost:8501.

3. Allow access to your webcam when prompted.

4. View the real-time object detection. Objects will be classified as "Ripe" or "Unripe" with confidence scores displayed.

5. Click the Stop button to end the video stream.

## Troubleshooting

- **Webcam Not Detected**: Ensure your webcam is connected and accessible.
- **Model Not Found**: Ensure the best.pt model file is in the correct path and properly trained.
- **Streamlit Errors**: Update Streamlit to the latest version using pip install --upgrade streamlit.


## Acknowledgments

- **Ultralytics** for the YOLO model and support tools.
- **Streamlit** for the interactive web app framework.
- **OpenCV** and **cvzone** for computer vision tools.

## License

This project is licensed under the MIT License. See the LICENSE file for more details. (Not Yet)

## Contact

For questions or feedback, feel free to open an issue or contact me.

    ```bash
    You can copy and paste this content into a `README.md` file for your project. Let me know if you need any modifications!
    ```