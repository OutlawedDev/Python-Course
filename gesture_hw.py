import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
os.environ["GLOG_minloglevel"] = "3"

import cv2
import mediapipe as mp
import numpy as np
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

current_filter = "NORMAL"

SEPIA_MATRIX = np.array([
    [0.272, 0.534, 0.131],
    [0.349, 0.686, 0.168],
    [0.393, 0.769, 0.189]
])

def apply_filter(img, f):
    if f == "SEPIA":
        return np.clip(cv2.transform(img, SEPIA_MATRIX), 0, 255).astype(np.uint8)
    elif f == "NEGATIVE":
        return cv2.bitwise_not(img)
    elif f == "CARTOON":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(gray, 7)
        edges = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        color = cv2.bilateralFilter(img, 9, 250, 250)
        return cv2.bitwise_and(color, color, mask=edges)
    elif f == "BRIGHTNESS":
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
        hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 1.25 + 20, 0, 255)
        return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    elif f == "INTENSITY":
        return cv2.convertScaleAbs(img, alpha=1.4, beta=0)

    return img

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()


prev_time = 0

print("\n Gesture Controls")
print("----------------------")
print("Index finger up == sepia")
print("Middle finger up == brightness")
print("Ring finger up == intensity")
print("Pinky finger up == cartoon")
print("Thumb + Index pinch = capture photo\n")

while True:

    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    capture = False

    if result.multi_hand_landmarks:

        hand_landmarks = result.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        lm = hand_landmarks.landmark

        thumb = (int(lm[4].x * w), int(lm[4].y * h))
        index = (int(lm[8].x * w), int(lm[8].y * h))
        middle = (int(lm[12].x * w), int(lm[12].y * h))
        ring = (int(lm[16].x * w), int(lm[16].y * h))
        pinky = (int(lm[20].x * w), int(lm[20].y * h))

        if abs(thumb[0] - index[0]) < 25 and abs(thumb[1] - index[1]) < 25:
            capture = True


        if index[1] < lm[6].y * h:
            current_filter = "SEPIA"
        elif middle[1] < lm[10].y * h:
            current_filter = "BRIGHTNESS"
        elif ring[1] < lm[14].y * h:
            current_filter = "INTENSITY"
        elif pinky[1] < lm[18].y * h:
            current_filter = "CARTOON"

    output = apply_filter(frame, current_filter)

    if capture:
        filename = f"photo_{int(time.time())}.jpg"
        cv2.imwrite(filename, output)
        print("saved:", filename)
        time.sleep(1)

    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time !=0 else 0
    prev_time = current_time

    cv2.putText(output, f"Fps: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.putText(output, f"Filter: {current_filter}", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Ai gesture camera", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
hands.close()
