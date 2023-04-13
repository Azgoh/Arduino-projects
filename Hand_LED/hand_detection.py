import cv2
import time
import math
import serial
import mediapipe as mp
from threading import Thread

port_name = "/dev/ttyACM0"
common_baudrate = 115200
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def connectToArduino():
    try: 
        arduino_serial = serial.Serial(port=port_name, baudrate=common_baudrate)
        time.sleep(1)
        print("Connection successfully established to port " + port_name)
        return arduino_serial
    except:
        print("Couldn't connect to port " + port_name)
        exit(0)

def captureVideo(arduino_serial):
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
            mpDraw.draw_landmarks(frame, results.multi_hand_landmarks[0], mpHands.HAND_CONNECTIONS)
            input = '%.0f'%(distance * 100)
            print(input)
            arduino_serial.write(input.encode())
            time.sleep(0.1)
            print(arduino_serial.readline()) 

        cv2.imshow("Video", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()
    arduino_serial.close()

if __name__ == "__main__": 
    arduino_serial = connectToArduino()
    Thread(target=captureVideo, args=(arduino_serial,)).start()
    
