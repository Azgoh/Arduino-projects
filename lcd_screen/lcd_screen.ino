#include <LiquidCrystal.h> 
int Contrast=0;
 LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  

byte Heart[8] = {
  0b00000,
  0b01010,
  0b11111,  
  0b11111,
  0b01110,
  0b00100,
  0b00000,
  0b00000
};

byte middleFinger[8] = {
  0b00000,
  0b00100,
  0b00100,
  0b00100,
  0b01110,
  0b11111,
  0b11111,
  0b00000 
};

 void setup()
 {
    analogWrite(6,Contrast);
     lcd.begin(16, 2);
     lcd.createChar(0, Heart);
     lcd.createChar(1, middleFinger);
     lcd.clear();

  } 
     void loop()
 { 
     lcd.clear();
     lcd.setCursor(6,0);
     lcd.print("Hey!");
     delay(1000);
     lcd.clear();
     lcd.home();
     lcd.print("wanna see a");
     lcd.setCursor(0,1);
     lcd.print("trick?");
     delay(5000);
     lcd.noDisplay();
     delay(1000);
     lcd.clear();
     lcd.home();
     lcd.setCursor(4,0);
     lcd.print("I ");
     lcd.write(byte(0));
     lcd.print(" you!");
     lcd.display();
     delay(5000);
 }
