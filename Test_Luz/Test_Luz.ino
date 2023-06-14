
int pin2=A1;
int i=0;

void setup() {
  Serial.begin(9600);
  pinMode(pin2, INPUT);
  // put your setup code here, to run once:

}

void loop() {
  while(i<2){
  int luz=analogRead(A1);
  float porcentaje_l=map(luz,1023,0,0,100);
  Serial.print(luz);
  Serial.print("\n");
  Serial.print(porcentaje_l);
  Serial.print("\n");
  i+=1;
  }
  // put your main code here, to run repeatedly:

}
