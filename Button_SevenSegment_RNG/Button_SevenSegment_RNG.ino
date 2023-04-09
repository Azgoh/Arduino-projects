#include <SevSeg.h>

SevSeg sevseg;
const int buttonPin = 10;
int lastButtonState;


void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, INPUT_PULLUP);
  lastButtonState = digitalRead(buttonPin);
  byte numDigits = 1;
  byte digitalPins[] = {};
  byte segmentPins[] = {6, 5, 2, 3, 4, 7, 8, 9};
  bool resistorsOnSegments = true;

  byte hardwareConfig = COMMON_CATHODE;
  sevseg.begin(hardwareConfig, numDigits, digitalPins, segmentPins, resistorsOnSegments);
  sevseg.setBrightness(90);
  randomSeed(analogRead(0));

}

void loop() {

  int currentButtonState = digitalRead(buttonPin);
  if(currentButtonState != lastButtonState){
    if(currentButtonState == LOW){
      sevseg.setNumber(random(0, 9));
      sevseg.refreshDisplay();
    }
    lastButtonState = currentButtonState;
  }
}
