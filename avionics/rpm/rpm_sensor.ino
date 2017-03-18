/*
Arduino RPM Sensor
by
Peter McCloud - McCloud Aero Corp (http://mccloudaero.com)

Inspired by:
Hall Effect Sensor Project on DIY Hacking (http://diyhacking.com)
by Arvind Sanjeev
*/


 volatile byte revolutions;
 unsigned int rpm;
 unsigned long timeold;
 void setup()
 {
   Serial.begin(115200);
   attachInterrupt(0, magnet_detect, RISING);//Initialize the intterrupt pin (Arduino digital pin 2)
   revolutions = 0;
   rpm = 0;
   timeold = 0;
 }
 void loop()//Measure RPM
 {
   if (revolutions >= 20) { 
     rpm = 60*1000/(millis() - timeold)*revolutions;
     timeold = millis();
     revolutions = 0;
     //Serial.println(rpm,DEC);
   }
 }
 void magnet_detect()//This function is called whenever a magnet/interrupt is detected by the arduino
 {
   revolutions++;
   // All of the following is for debugging only
   Serial.println("detect");
   // Blink the LED on Interupt
   digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
   delay(1000);                       // wait for a second
   digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW

 }
