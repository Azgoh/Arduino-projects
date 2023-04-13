import cv2
import time
import serial
import mediapipe as mp
from threading import Thread

port_name = "/dev/ttyACM0"
common_baudrate = 9600
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
        handCount = 0
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                handCount += 1   
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = frame.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 20:
                        cv2.circle(frame, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                mpDraw.draw_landmarks(frame, handLms, mpHands.HAND_CONNECTIONS)
            input = bytes(str(handCount), "UTF-8")
            arduino_serial.write(input)
            time.sleep(0.1)
            print(arduino_serial.readline())
        else: 
            arduino_serial.write(bytes(str(handCount), "UTF-8")) 
            time.sleep(0.1) 

        cv2.imshow("Video", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break

    cap.release()
    cv2.destroyAllWindows()
    arduino_serial.close()

if __name__ == "__main__": 
    arduino_serial = connectToArduino()
    Thread(target=captureVideo, args=(arduino_serial,)).start()
    
