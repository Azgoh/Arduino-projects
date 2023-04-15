#include <Servo.h>

Servo servo;

void setup() {
  // put your setup code here, to run once:
  servo.attach(8);
  servo.write(0);

}

void loop() {
  // put your main code here, to run repeatedly:
  for(int angle=0; angle<=180; angle++){
    servo.write(angle);
    delay(15);
  }

  for(int angle=180; angle>=0; angle--){
    servo.write(angle);
    delay(15);
  }
  
  exit(0);
  
}
