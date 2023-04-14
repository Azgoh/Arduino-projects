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
    int brightness = Serial.readStringUntil('\n').toInt();
    Serial.println(brightness);
    analogWrite(LED_PIN, brightness);
  }
}
