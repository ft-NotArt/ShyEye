# 👁️ **ShyEye** #

### Our project took place in a one week workshop between students from 42, a coding school and ESADHAR fine arts (Le Havre, France) ###

## MAIN PROJECT ##

We decided to develop the idea of social anxiety through an AI.\
To put a human problem within the mind of a robot, basically.\
We have printed in 3D an eye, that evoques the sight, and to put a program in it that makes him reacts weirdly to people staring at him.\
With the use of a webcam linked to an Arduino and a python program, we were able to spot faces.

## CODE ##

The arduino board handles two Servo motors, allowing the eye to move\
The python program part is here to record a video with a webcam and pass its data to an c2v pre-trained AI model that detect faces. It then transmit certain values to the arduino board listening on port to knowin which direction it has to incline the eye to track people



## Dependencies ##

## Items ##


## ELECTRONIC SET-UP

|  Arduino pins  | Electronic component |
|----------------|:--------------------:|
| D10  |  Servo Motors Y digit  |
| D9   |  Servo Motors X digit  |







## 3D DESIGN ##

We designed the pieces on Fusion.\
Transfered the files on Curra to be able to print the different pieces.\
The eye isn’t a complet ball to be able to connect everything together.\
The system got put together with screws and a set square who welcomes the servo motors.\
\
The complicated part was to visualized the right sizes for all pieces, to make everything connect together.\
The diameter of the eye being a bit small, it had to be really precise.






