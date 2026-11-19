// C++ code
//
unsigned int napon_mV = 3750;
unsigned int kapacitet_mAh = 2600;
float naponV;
float kapacitet_Ah;
unsigned long ukupna_energija;


void setup()
{
Serial.begin(9600);
  ukupna_energija = (unsigned long)napon_mV * kapacitet_mAh;
  
  Serial.print("Ukupna energija:");
  Serial.println(ukupna_energija);
  
  Serial.begin(9600);
  kapacitet_Ah = (float)kapacitet_mAh / 1000;
  
  Serial.print("Kapacitet u Ah je: ");
  Serial.println(kapacitet_Ah);
}

void loop()
{
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000); // Wait for 1000 millisecond(s)
}
