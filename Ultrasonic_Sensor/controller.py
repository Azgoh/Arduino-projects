import serial
import time
import pyautogui

port_name = "/dev/ttyACM0"
common_baudrate = 9600

arduino_serial = serial.Serial(port_name, common_baudrate)
start_time = time.time()
time.sleep(2)

if(arduino_serial.is_open):
    print("Connection established to" + arduino_serial.name)
else: 
    print("Could not establish connection to" + arduino_serial.name)

time.sleep(1)

while True:
    incoming_data = str(arduino_serial.readline())
    print(incoming_data)
    if('Play/Pause' in incoming_data):
        pyautogui.typewrite(['space'], 0.2)
    if(time.time() - start_time > 60):
        break

arduino_serial.close()
print("Connection ended after " + str(int(time.time() - start_time)) + " seconds")