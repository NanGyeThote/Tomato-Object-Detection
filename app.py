import streamlit as st
import cv2
import cvzone
import math
from ultralytics import YOLO

# Initialize YOLO model
model = YOLO('best.pt')
classNames = ["Unripe", "Ripe"]

# Function to perform object detection and display results
def detect_objects(img):
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0].int().tolist()
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h))

            conf = math.ceil(box.conf[0] * 100) / 100
            cls = int(box.cls[0])

            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=2)

    return img

# Main Streamlit application
def main():
    st.title('YOLO Object Detection with Streamlit')

    # Capture video from webcam or file
    cap = cv2.VideoCapture(0)
    cap.set(3, 720)
    cap.set(4, 480)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error('Failed to capture image from webcam.')
            break

        frame = cv2.flip(frame, 1)
        detected_frame = detect_objects(frame)

        # Display the image with Streamlit
        st.image(detected_frame, channels="BGR", use_column_width=True)

        # Check for user input to stop the stream
        if st.button('Stop'):
            break

    cap.release()

if __name__ == '__main__':
    main()