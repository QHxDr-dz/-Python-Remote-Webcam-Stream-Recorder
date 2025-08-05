from flask import Flask, Response
import cv2

app = Flask(__name__)


cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('recorded.avi', fourcc, 20.0, (640, 480))

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
          
            out.write(frame)

            
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

          
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
