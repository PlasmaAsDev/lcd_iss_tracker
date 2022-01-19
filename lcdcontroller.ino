#include <LiquidCrystal.h>

const int rs = 7, en = 6, d4 = 5, d5 = 4, d6 = 3, d7 = 2; //Setting up the lcd


LiquidCrystal lcd(rs, en, d4, d5, d6, d7); //Initialize the lcd class


void setup() {
  lcd.begin(16, 2); //Beginning the lcd, 16x2
  Serial.begin(9600); //Beginning the Serial
  Serial.setTimeout(200);

  lcd.setCursor(0,0);
  lcd.print("Lon = ");
  lcd.setCursor(0,1);
  lcd.print("Lat = ");

  Serial.println("Arduino started, you have to send data with the script specified in the repository.");
  Serial.println("https://github.com/PlasmaAsDev/lcd_iss_tracker");
}


void loop() {
  while(!Serial.available());

  lcd.setCursor(6,0);
  lcd.print("                        ");
  lcd.setCursor(6,1);
  lcd.print("                        ");

  String incommingStr = Serial.readStringUntil('\n'); //Read the complete string

  String lon = incommingStr.substring(0,7); //Divide the received string in the first 7 characters

  String lat = incommingStr.substring(7);

  lcd.setCursor(6,0); 
  lcd.print(lon); // Print the longitude value on lcd

  lcd.setCursor(6,1);
  lcd.print(lat); // Print the latitude value on lcd

  delay(500);
}
