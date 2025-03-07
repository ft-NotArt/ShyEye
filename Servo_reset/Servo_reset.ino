#include "Servo.h"

#define START_POS 90

Servo servoX ;
Servo servoY ;

void setup() {
    servoX.attach(9) ;  // attache le servoX au pin 9
    servoY.attach(10) ; // attache le servoY au pin 10

    servoX.write(START_POS) ;
    servoY.write(START_POS) ;
    delay(1000) ;
}

void loop() {

}