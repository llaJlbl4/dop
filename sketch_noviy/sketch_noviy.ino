char a;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  a = Serial.read();
  if (a == '1'){
  digitalWrite(13, 1);
  delay(1000);
  Serial.println("ON");

  digitalWrite(13, 0);
  delay(500);
  Serial.println("OFF");
  }

  if (a == '2'){
  digitalWrite(13, 1);
  delay(2000);
  Serial.println("ON");

  digitalWrite(13, 0);
  delay(200);
  Serial.println("OFF");
  }

  if (a == '0'){
  digitalWrite(13, 1);
  delay(200);
  Serial.println("ON");

  digitalWrite(13, 0);
  delay(200);
  Serial.println("OFF");
  }
}
