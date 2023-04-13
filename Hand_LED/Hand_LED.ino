const int LED_PIN = 5;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(LED_PIN, INPUT);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  // put your main code here, to run repeatedly
  if(Serial.available()){
    int distance = Serial.readStringUntil('\n').toInt();
    int brightness = distance * 5;
    if(brightness > 255) brightness = 255;
    else if(distance < 5) brightness = 0;
    Serial.println(brightness);
    analogWrite(LED_PIN, brightness);
  }
}
