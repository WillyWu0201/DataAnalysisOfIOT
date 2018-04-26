int photocellPin = 2;
int photocellVal = 0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  photocellVal = analogRead(photocellPin);
  Serial.println(photocellVal);
  delay(1000);
}
