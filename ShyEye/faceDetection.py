import cv2
import serial
import time
import random

# Used for debug mainly, set to True to see what the camera is recording
DRAW_CAMERA = True


"""
	These are just indications used to understand what value is passed through Serial to arduino
	In the arduino code, same values will be used but as defines
	Setting those in this order enables me to only do +1/+2 to choose up or down in addition to left/right direction
"""

# Move to the left
SERVO_LMOV = 0
SERVO_LUMOV = 1
SERVO_LDMOV = 2

# Move to the right
SERVO_RMOV = 3
SERVO_RUMOV = 4
SERVO_RDMOV = 5

# Don't move x axis
SERVO_NOMOV = 6
SERVO_UMOV = 7
SERVO_DMOV = 8


SERVO_SPD = 10

def draw_square(frame, faces, color):
	for (x, y, w, h) in faces:
		face_region = frame[y:y+h, x:x+w]
		cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1)
	return frame

# Returns the opposite of a given move
# for example, the opposite of left move would be right move
def reverse_move(move) :
	switch = {
		SERVO_LMOV : SERVO_RMOV,
		SERVO_LUMOV : SERVO_RDMOV,
		SERVO_LDMOV : SERVO_RUMOV,
		SERVO_RMOV : SERVO_LMOV,
		SERVO_RDMOV : SERVO_LUMOV,
		SERVO_RUMOV : SERVO_LDMOV,
		SERVO_UMOV : SERVO_DMOV,
		SERVO_DMOV : SERVO_UMOV,
	}
	return switch.get(move, SERVO_NOMOV)


arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
side_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
detected_faces = []
detected_profiles = []


ret, frame = video_capture.read()
if ret:
	frameH, frameW = frame.shape[:2]
	eyeX = int (frameW / 2)
	eyeY = int (frameH / 2)


while True:
	ret, frame = video_capture.read()
	if not ret:
		break

	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	detected_faces = faces
	faces = side_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	detected_profiles = faces

	target = [int ((frameW / 2) - 10), int ((frameH / 2) - 10), 20, 20]
	eyeDir = SERVO_NOMOV
	if len(detected_faces) >= 3 :
		print("anxieux")
		anxiety_queue = []
		for i in range(3) :
			anxiety_queue.append(random.choice([SERVO_LMOV, SERVO_LUMOV, SERVO_LDMOV, SERVO_RMOV, SERVO_RUMOV, SERVO_RDMOV, SERVO_UMOV, SERVO_DMOV]))
			arduino.write(bytes(f"{anxiety_queue[i]}", "utf-8"))
		for i in range(3) :
			arduino.write(bytes(f"{reverse_move(anxiety_queue[i])}", "utf-8"))
	elif len(detected_profiles) != 0 and len(detected_faces) != 0 :
		arduino.write(bytes(f"{SERVO_NOMOV}", "utf-8"))
	else :
		if len(detected_profiles) != 0 and len(detected_faces) == 0 :
			# get target as the biggest face detected
			for face in detected_profiles :
				if face[3] > target[3] : # deep copy as I want to modify target w/out modifying detected_profiles
					target[0] = face[0]
					target[1] = face[1]
					target[2] = face[2]
					target[3] = face[3]

			# define target as the center of selected face
			target[0] = int (target[0] + (target[2] / 2) - 10)
			target[1] = int (target[1] + (target[3] / 2) - 10)
			target[2] = 20
			target[3] = 20

		# adjust the 'eye' position as the camera turn around
		if eyeX < target[0] or eyeX > (target[0] + target[2]) :
			if eyeX < target[0] :
				eyeX += SERVO_SPD
				eyeDir = SERVO_LMOV
			else :
				eyeX -= SERVO_SPD
				eyeDir = SERVO_RMOV
		else :
			eyeDir = SERVO_NOMOV
		if eyeY < target[1] or eyeY > (target[1] + target[3]) :
			if eyeY < target[1] :
				eyeY += SERVO_SPD
				eyeDir += 2 # As moving down values had been set up to horizontal move + 2
			else :
				eyeY -= SERVO_SPD
				eyeDir += 1 # As moving up values had been set up to horizontal move + 1
		
		arduino.write(bytes(f"{eyeDir}", "utf-8"))


	if DRAW_CAMERA :
		# draw detected_faces/profiles on green/blue
		frame = draw_square(frame, detected_faces, (0, 255, 0))
		frame = draw_square(frame, detected_profiles, (255, 0, 0))

		# draw target rectangle in red
		cv2.rectangle(frame, (target[0], target[1]), (target[0] + target[2], target[1] + target[3]), (0, 0, 255), 1)
	
		# draw crosshair in white
		cv2.rectangle(frame, (eyeX - 5, eyeY), (eyeX + 5, eyeY), (255, 255, 255), 1)
		cv2.rectangle(frame, (eyeX, eyeY - 5), (eyeX, eyeY + 5), (255, 255, 255), 1)

		# open a window and show recorded video
		cv2.imshow("Faces", frame)

	if cv2.waitKey(1) != -1:
		break


video_capture.release()
cv2.destroyAllWindows()
