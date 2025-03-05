#include "Servo.h"

Servo servo1 ;
Servo servo2 ;

void setup() {
    servo1.attach(9) ;  // attache le servo1 au pin 9
    servo2.attach(10) ; // attache le servo2 au pin 10

    servo1.write(0) ;
    servo2.write(0) ;
    delay(1000) ;

}

void loop() {
  static int a = 0 ;
  a += 5 ;
  servo1.write(a) ;
  servo2.write(a) ;
  delay(100) ;
  if (a == 0)
    delay(1000) ;
  else if (a == 180)
    a = -5 ;
}