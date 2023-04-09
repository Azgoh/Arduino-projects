#include <IRremote.hpp>

const int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
const int LED = 6;
int baseBrightness = 51;

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop() {
  if(irrecv.decode()){
    Serial.println(irrecv.decodedIRData.decodedRawData, HEX);
    if(irrecv.decodedIRData.decodedRawData == 0xFD020707){
      if(digitalRead(LED) == 0){
        digitalWrite(LED, HIGH);
      }
      else{
        digitalWrite(LED, LOW);
      }
    }
    else if(irrecv.decodedIRData.decodedRawData == 0xF8070707 && baseBrightness <= 205 && digitalRead(LED) == 1){
      baseBrightness += 50;
      analogWrite(LED, baseBrightness);  
    }
    else if(irrecv.decodedIRData.decodedRawData == 0xF40B0707 && baseBrightness >= 50 && digitalRead(LED) == 1){
      baseBrightness -= 50;
      analogWrite(LED, baseBrightness);
    }
    delay(100);
    irrecv.resume();
  }
}

//FD020707 turn on led with power button
//F40B0707 turn off led with volume down button
