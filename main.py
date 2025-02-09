from flask import Flask, render_template, Response
import os
import cv2
import mediapipe as mp

app = Flask(__name__)

mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

emoji = cv2.imread("angry_emoji.png", cv2.IMREAD_UNCHANGED)

if emoji.shape[-1] == 4:  # Convertir si tiene canal alpha
    emoji = cv2.cvtColor(emoji, cv2.COLOR_BGRA2BGR)

cap = cv2.VideoCapture(0)  # Usa la cámara de la PC donde corre Flask

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(rgb_frame)

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x, y, w_box, h_box = (int(bboxC.xmin * w), int(bboxC.ymin * h),
                                      int(bboxC.width * w), int(bboxC.height * h))

                x2 = min(x + w_box, w)
                y2 = min(y + h_box, h)

                if x >= 0 and y >= 0 and x2 > x and y2 > y:
                    resized_emoji = cv2.resize(emoji, (x2 - x, y2 - y))
                    frame[y:y2, x:x2] = resized_emoji[:y2-y, :x2-x, :3]

                    cv2.putText(frame, "No puedes mirar a otra!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.9, (0, 0, 255), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=5000, debug=True)
