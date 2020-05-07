int R1=8;
int BUZZER=9;


char ch;
void setup()
{


  Serial.begin(9600);//192.168.4.1//

  pinMode(R1, OUTPUT);
   pinMode(BUZZER, OUTPUT);
 digitalWrite(R1,LOW);
  digitalWrite(BUZZER,LOW);

  Serial.print("EYE TRACKING PASSWORD");
  delay(500);
  
}
void loop()
{
  
SerialEvent();

}
char Serial_read(void)
{
      char ch;
      while(Serial.available() == 0);
      ch = Serial.read(); 
      return ch;
}
void SerialEvent()
{
      if (Serial.available() > 0)
      {
          ch = Serial_read();
      
          Serial.print(ch);
          
          if (ch == '1')
          {
              Serial.println("LOCK OPEN");
              digitalWrite(R1, HIGH);
              delay(1000);
          }
          if (ch == '2')
          {
              Serial.println("PASSWORD MISSMATCH");
              digitalWrite(R1, LOW);
               digitalWrite(BUZZER, HIGH);
              delay(1000);
          }
        
          
      }
 
}
 
