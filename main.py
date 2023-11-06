import cv2
import os
import shutil


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

# Define a function to capture a video snippet
def capture_video():
    video_path = os.path.join("SecurityCam", "captured_video.avi")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))  # Adjust resolution and frame rate

    while True:
        ret, frame = cap.read()
        if ret:
            out.write(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to stop capturing video
                break
        else:
            break

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
            capture_video()

    cap.release()

if __name__ == "__main__":
    main()
