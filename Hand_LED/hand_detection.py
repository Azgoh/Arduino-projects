import cv2
import time
import math
import mediapipe as mp
from serial import Serial
from threading import Thread

port_name = "/dev/ttyACM0"
common_baudrate = 115200
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def connect_to_arduino():
    try: 
        arduino_serial = Serial(port=port_name, baudrate=common_baudrate)
        time.sleep(1)
        print("Connection successfully established to port " + port_name)
        return arduino_serial
    except:
        print("Couldn't connect to port " + port_name)
        exit(0)

def capture_video(arduino_serial):
    min_dist, max_dist = 5,50
    while True: 
        _, frame = cap.read()
        imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        results = hands.process(imageRGB)
        if results.multi_hand_landmarks:
            thumb_point, index_point = 0, 0 
            for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
                if id == 4: 
                    thumb_point = (lm.x, lm.y)
                elif id == 8: 
                    index_point = (lm.x, lm.y)
            distance = math.sqrt((index_point[0] - thumb_point[0])**2 + (index_point[1] - thumb_point[1])**2)
            mp_draw.draw_landmarks(frame, results.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
            distance = int(distance* 100)
            if distance < min_dist:
                min_dist = distance
            if distance > max_dist: 
                max_dist = distance
            brightness = calculate_brightness(distance, min_dist, max_dist)
            arduino_serial.write(brightness.encode()) 

        cv2.imshow("Video", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()
    arduino_serial.close()

def calculate_brightness(distance, min_dist, max_dist): 
    brightness = (255*distance) / (max_dist - min_dist)
    if brightness > 255: 
        return str(255)
    elif brightness < 25: 
        return str(0)
    return '%.0f'%brightness

if __name__ == "__main__": 
    arduino_serial = connect_to_arduino()
    Thread(target=capture_video, args=(arduino_serial,)).start()
    
