import cv2
import os
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from datetime import datetime

if not os.path.exists("SecurityCam"):
    os.makedirs("SecurityCam")  # ye basically folder banata hai

cap = cv2.VideoCapture(0)


def capture_photo():
    ret, frame = cap.read()
    if ret:
        timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        photo_path = os.path.join("SecurityCam", f"captured_photo_{timestamp}.jpg")
        cv2.imwrite(photo_path, frame)
        print("Photo captured:", photo_path)
    else:
        print("Failed to capture photo")


def capture_video(duration):
    video_path = os.path.join("SecurityCam", f"captured_video_{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.avi")
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))
    start_time = time.time()
    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if ret:
            out.write(frame)

    out.release()
    print("Video captured:", video_path)


def send_email_notification(image_path):
    sender_email = "mrid.sawant@gmail.com"
    sender_password = "mridgandh"
    recipient_email = "ssawant@igpetro.com"

    subject = "Security Alert"
    text = "Unauthorized access detected at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))

    img_data = open(image_path, 'rb').read()
    image = MIMEImage(img_data, name=os.path.basename(image_path))
    msg.attach(image)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print("Email notification sent.")
    except Exception as e:
        print("Failed to send email notification:", str(e))


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
            send_email_notification(os.path.join("SecurityCam", "captured_photo.jpg"))

    cap.release()


if __name__ == "__main__":
    main()
