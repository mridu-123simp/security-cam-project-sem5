#all the comments are for reference only by me not for anyone else :)
import cv2
import os
import time

# Create the SecurityCam folder if it doesn't exist
if not os.path.exists("SecurityCam"):
    os.makedirs("SecurityCam")

# Set up the webcam
cap = cv2.VideoCapture(0)  # 0 indicates the default webcam

# Define a function to capture a photo
def capture_photo():
    ret, frame = cap.read()
    if ret:
        photo_path = os.path.join("SecurityCam", "captured_photo.jpg")
        cv2.imwrite(photo_path, frame)
        print("Photo captured:", photo_path)
    else:
        print("Failed to capture photo")

# Define a function to capture a video snippet for a specified duration
def capture_video(duration):
    video_path = os.path.join("SecurityCam", "captured_video.avi")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))  # Adjust resolution and frame rate

    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)

    out.release()
    print("Video captured:", video_path)

# Main program loop
def main():
    while True:
        password = input("Enter the password: ")
        if password == "2004":
            print("Access granted")

            break
        else:
            print("Access denied")
            capture_photo()
            capture_video(5)  # Capture video for 5 seconds

    cap.release()

if __name__ == "__main__":
    main()
