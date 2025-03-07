# 👁️ **ShyEye** #

### Our project took place in a one week workshop between students from 42, a coding school and ESADHAR fine arts (Le Havre, France) ###

<br>

## MAIN PROJECT ##

We decided to develop the idea of social anxiety through an AI.\
To put a human problem within the mind of a robot, basically.\
We have printed in 3D an eye, that evoques the sight, and to put a program in it that makes him reacts weirdly to people staring at him.\
With the use of a webcam linked to an Arduino and a python program, we were able to spot faces.

![eye](https://github.com/user-attachments/assets/b0876501-04a4-4ab6-b07d-835ce6e18e3a)

<br>

## CODE ##

The arduino board handles two Servo motors, allowing the eye to move\
The python program part is here to record a video with a webcam and pass its data to an c2v pre-trained AI model that detect faces. It then transmit certain values to the arduino board listening on port to know in which direction it has to incline the eye to track people

<br>

## Dependencies ##

For the program to work, you need two python libraries\
Run : 
- ```python3 -m venv venv```
- ```pip install opencv-python```
- ```pip install pyserial```

<br>

## Items ##

- [arduino nano 33 ble](https://store.arduino.cc/en-fr/products/arduino-nano-33-ble?srsltid=AfmBOooPKgtWtLVe8zBSpjlLMJosrKHyBQENk51W_Wd9E3Dk7IboJRVS)
- [2 Servo motors](https://store.arduino.cc/products/feetech-mini-servo-motor-120-degrees-9g?queryID=undefined)
- [a breadboard](https://store.arduino.cc/products/breadboard-400-contacts?queryID=undefined)

<br>

## ELECTRONIC SET-UP

|  Arduino pins  | Electronic component |
|----------------|:--------------------:|
| D10  |  Servo Motors Y digit  |
| D9   |  Servo Motors X digit  |

![elec2](https://github.com/user-attachments/assets/00474872-c965-48a5-9593-c681406c6e20)

There's a lot of wires just to have a 3.3V and a 5V supply, but we don't use the 3.3V, so don't overlook it...

<br>

## 3D DESIGN ##

We designed the pieces on Fusion.\
Transfered the files on Curra to be able to print the different pieces.\
The eye isn’t a complet ball to be able to connect everything together.\
![behind_eye](https://github.com/user-attachments/assets/f3d2f328-aa79-45da-a817-642c24da24a2)
The system got put together with screws and a set square who welcomes the servo motors.\
\
The complicated part was to visualized the right sizes for all pieces, to make everything connect together.\
The diameter of the eye being a bit small, it had to be really precise.
