import cv2
import serial

SERVO_SPD = 2

def draw_square(frame, faces, color):
	for (x, y, w, h) in faces:
		face_region = frame[y:y+h, x:x+w]
		cv2.rectangle(frame, (x, y), (x + w, y + h), color, 1)
	return frame


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

	frame = draw_square(frame, detected_faces, (0, 255, 0))
	frame = draw_square(frame, detected_profiles, (255, 0, 0))

	target = [int ((frameW / 2) - 10), int ((frameH / 2) - 10), 20, 20]
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
		else :
			eyeX -= SERVO_SPD
	if eyeY < target[1] or eyeY > (target[1] + target[3]) :
		if eyeY < target[1] :
			eyeY += SERVO_SPD
		else :
			eyeY -= SERVO_SPD


	# draw target rectangle in red
	cv2.rectangle(frame, (target[0], target[1]), (target[0] + target[2], target[1] + target[3]), (0, 0, 255), 1)
	
	# draw crosshair in white
	cv2.rectangle(frame, (eyeX - 5, eyeY), (eyeX + 5, eyeY), (255, 255, 255), 1)
	cv2.rectangle(frame, (eyeX, eyeY - 5), (eyeX, eyeY + 5), (255, 255, 255), 1)



	cv2.imshow("Faces", frame)

	if cv2.waitKey(1) != -1:
		break


video_capture.release()
cv2.destroyAllWindows()
