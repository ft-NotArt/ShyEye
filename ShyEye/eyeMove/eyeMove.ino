#include "Servo.h"

/*
	These are just indications used to understand what value is passed through Serial to Arduino
*/

// Move to the left
#define SERVO_LMOV 0
#define SERVO_LUMOV 1
#define SERVO_LDMOV 2

// Move to the right
#define SERVO_RMOV 3
#define SERVO_RUMOV 4
#define SERVO_RDMOV 5

// Don't move x axis
#define SERVO_NOMOV 6
#define SERVO_UMOV 7
#define SERVO_DMOV 8

#define LOOK_LEFT -45
#define LOOK_RIGHT 45
#define LOOK_UP 45
#define LOOK_DOWN -45

#define START_POS 90

Servo servoX;
Servo servoY;
int eyeDir;
bool isServoXAttached = true;
bool isServoYAttached = true;

void setup() {
  servoX.attach(9);  // Attach servoX to pin 9
  servoY.attach(10); // Attach servoY to pin 10

  servoX.write(START_POS);
  servoY.write(START_POS);
  delay(1000);

  Serial.begin(9600);
  Serial.setTimeout(1);

  // Used for debugging
  pinMode(LED_BUILTIN, OUTPUT);
}

void stopServo(Servo &servo, bool &isAttached) {
  if (isAttached) {  // Only detach if it's currently attached
    servo.detach();
    isAttached = false;
  }
}

void moveServo(Servo &servo, int angle, bool &isAttached, int pin) {
  if (!isAttached) {  // Only attach if it's currently detached
    servo.attach(pin);
    isAttached = true;
  }
  servo.write(angle);
}

void loop() {
  while (!Serial.available());
  eyeDir = Serial.readString().toInt();

  switch (eyeDir) {
    case SERVO_LMOV:
      moveServo(servoX, START_POS + LOOK_LEFT, isServoXAttached, 9);
      stopServo(servoY, isServoYAttached);
      break;

    case SERVO_LUMOV:
      moveServo(servoX, START_POS + LOOK_LEFT, isServoXAttached, 9);
      moveServo(servoY, START_POS + LOOK_UP, isServoYAttached, 10);
      break;

    case SERVO_LDMOV:
      moveServo(servoX, START_POS + LOOK_LEFT, isServoXAttached, 9);
      moveServo(servoY, START_POS + LOOK_DOWN, isServoYAttached, 10);
      break;

    case SERVO_RMOV:
      moveServo(servoX, START_POS + LOOK_RIGHT, isServoXAttached, 9);
      stopServo(servoY, isServoYAttached);
      break;

    case SERVO_RUMOV:
      moveServo(servoX, START_POS + LOOK_RIGHT, isServoXAttached, 9);
      moveServo(servoY, START_POS + LOOK_UP, isServoYAttached, 10);
      break;

    case SERVO_RDMOV:
      moveServo(servoX, START_POS + LOOK_RIGHT, isServoXAttached, 9);
      moveServo(servoY, START_POS + LOOK_DOWN, isServoYAttached, 10);
      break;

    case SERVO_UMOV:
      stopServo(servoX, isServoXAttached);
      moveServo(servoY, START_POS + LOOK_UP, isServoYAttached, 10);
      break;

    case SERVO_DMOV:
      stopServo(servoX, isServoXAttached);
      moveServo(servoY, START_POS + LOOK_DOWN, isServoYAttached, 10);
      break;

    default:
      stopServo(servoX, isServoXAttached);
      stopServo(servoY, isServoYAttached);
      break;
  }
}

