#include "Servo.h"

Servo servo1 ;
Servo servo2 ;

void setup() {
   servo1.attach(9);  // attache le servo1 au pin 9
   servo2.attach(10); // attache le servo2 au pin 10
}

void loop() {

  servo1.write(0) ;
  servo2.write(0) ;
}