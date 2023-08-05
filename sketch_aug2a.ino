int pin1 = 6;
int pin2 = 5;
int pin3 = 4;
int delayseg= 249;

void setup() {
  pinMode(pin1, OUTPUT); // Configura el pin 13 como salida
  pinMode(pin2, OUTPUT); // Configura el pin 13 como salida
  pinMode(pin3, OUTPUT); // Configura el pin 13 como salida
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read(); // Leer el comando enviado por Python
    if (comando == '1') {
      digitalWrite(pin1, HIGH); // Encender el LED
      delay(delayseg);
      digitalWrite(pin1, LOW);
      delay(delayseg);
    } else if (comando == '2') {
      digitalWrite(pin2, HIGH); // Encender el LED
      delay(delayseg);
      digitalWrite(pin2, LOW);
      delay(delayseg);
    } else if (comando == '3'){
      digitalWrite(pin3, HIGH); // Encender el LED
      delay(delayseg);
      digitalWrite(pin3, LOW);
      delay(delayseg);
    }
  }
  
}
