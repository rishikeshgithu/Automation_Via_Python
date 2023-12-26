import cv2
import easyocr
import pyttsx3
import os
from datetime import datetime

# Create a folder to save images if it doesn't exist
images_folder = 'images'
if not os.path.exists(images_folder):
    os.makedirs(images_folder)

# Initialize EasyOCR reader and TTS engine
reader = easyocr.Reader(['en'])
engine = pyttsx3.init()

# Open the default camera (0 or -1) or a specific camera (1, 2, etc.)
cap = cv2.VideoCapture(0)  # Change the index if required

while True:
    ret, frame = cap.read()  # Read frame from the camera
    if not ret:
        break

    # Perform OCR on the frame
    result = reader.readtext(frame)

    # Display the results on the frame
    for detection in result:
        text = detection[1]
        bbox = detection[0]

        # Convert bounding box coordinates to integers
        bbox = [tuple(map(int, point)) for point in bbox]

        # Draw bounding boxes and text on the frame
        cv2.rectangle(frame, bbox[0], bbox[2], (0, 255, 0), 2)
        cv2.putText(frame, text, (bbox[0][0], bbox[0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow('Camera OCR', frame)

    # Extract and speak recognized text
    recognized_text = ""
    for detection in result:
        recognized_text += detection[1] + " "

    # Get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Save the image with the timestamp in the 'images' folder
    image_path = os.path.join(images_folder, f"{current_datetime}.jpg")
    cv2.imwrite(image_path, frame)

    # Save recognized text with image name and timestamp in a text file
    text_file_path = os.path.join(images_folder, "recognized_text.txt")
    with open(text_file_path, "a") as text_file:
        text_file.write(f"Image Name: {current_datetime}.jpg\n")
        text_file.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        text_file.write(f"Recognized Text: {recognized_text}\n\n")

    # Speak recognized text using TTS
    engine.say(recognized_text)
    engine.runAndWait()

    # Wait for key press and break loop if 'q' is pressed
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

# Release the camera
cap.release()
cv2.destroyAllWindows()
