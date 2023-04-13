const int LED_PIN = 5;
int input = 1;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.setTimeout(1);
  pinMode(LED_PIN, INPUT);
  digitalWrite(LED_PIN, LOW);
}

void loop() {
  // put your main code here, to run repeatedly
  if(Serial.available()){
    input = Serial.readString().toInt();
    Serial.println(input);
    analogWrite(LED_PIN, input*100);
  }
}
