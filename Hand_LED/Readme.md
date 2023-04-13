## Control LED Brightness With Your Thumb and Index Fingers
This is my attempt on controlling the brightness of an LED connected to an Arduino UNO, based on the distance between the thumb and the index. The bigger the distance, the brighter the LED gets. 

## Running the application
In order to run the application you will need to upload the `Hand_LED.ino` code to your arduino, to which you will need to have connected an LED to **PIN 5**. Then, in order to run the python script, you will need to install the python libraries `opencv` and `mediapipe`. Please note that the `port_name` in the script might be different in your case, so you will need to change that accordingly. Once you've completed the aforementioned steps, run the following command: 
```bash
python3 hand_detection.py
```

A live video using your webcam should pop up. If you show your hand to the camera, landmarks will be drawn on it and the script will start tracking the distance between your thumb and your index fingers. The LED's brightness can now be controlled by a simple movement of those two fingers.

## Terminating the script
If you wish to terminate the video and the script as a whole, either press **Q** when focused on the video, or alternatively **Ctrl+C** on your terminal.