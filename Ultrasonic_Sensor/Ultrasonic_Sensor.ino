const int trigPin = 9;
const int echoPin = 10;
const int buzzerPin = 7;
const int buzzerDuration = 500;
float duration, distance;

void setup() {
  
  pinMode(trigPin, OUTPUT);  
  pinMode(echoPin, INPUT);  
  Serial.begin(9600);

}

void loop() {
  
  calculateDistance();

  if(distance <= 10){
    Serial.println("Play/Pause");
  }
  while(distance <= 10){
    tone(buzzerPin, 1400, buzzerDuration);
    calculateDistance();
  }

  noTone(buzzerPin);

  delay(100); 

}

void calculateDistance(){
  if(millis() > 300000) exit(0);
  digitalWrite(trigPin, LOW); //setting the trigger pin to low to avoid any sonic cycles 
  delayMicroseconds(2);  
  digitalWrite(trigPin, HIGH);  //setting it to high with a 10us delay sends out an 8 cycle sonic burst
  delayMicroseconds(10);  
  digitalWrite(trigPin, LOW); 

  duration = pulseIn(echoPin, HIGH);  //counts the time which the echo pin remains high, which is determined by how long the sound waves were travelling for
  distance = (duration*.0343)/2;  //distance = (duration * speedOfSound)/2
  Serial.print("Distance: ");  
  Serial.println(distance);  
}
