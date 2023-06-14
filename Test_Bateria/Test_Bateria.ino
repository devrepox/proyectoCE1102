int pin=A0;
int pin2=A1;
float bateria;
int luz;
float porcentaje=0;
float voltaje=0;
int i=0;
void setup() {
  Serial.begin(9600);
  pinMode(pin, INPUT);
  pinMode(pin2, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  while(i<2){
  bateria=analogRead(pin);
  Serial.print(bateria);
  Serial.print("\n");
  voltaje=(6*bateria/530.0);
  Serial.print(voltaje);
  Serial.print("\n");
  porcentaje=(voltaje/6.0)*100;
  Serial.print(porcentaje);
  Serial.print("\n");
  i+=1;
  }
  // put your main code here, to run repeatedly:

}
