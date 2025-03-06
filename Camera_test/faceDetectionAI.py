import cv2

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


while True:
	ret, frame = video_capture.read()
	if not ret:
		break

	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	detected_faces = faces
	faces = side_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
	detected_profiles = faces

	target = [0, 0, 0, 0]
	if len(detected_faces) != 0 :
		for face in detected_faces :
			if face[3] > target[3] :
				target = face
	
	print(f"{target[3]}")

	# print(f"midH={frameH} midW={frameW} {len(detected_faces)} {len(detected_profiles)} ")

	frame = draw_square(frame, detected_faces, (0, 255, 0))
	frame = draw_square(frame, detected_profiles, (255, 0, 0))

	if len(detected_faces) != 0 :
		targetX = int (target[0] + (target[2] / 2))
		targetY = int (target[1] + (target[3] / 2))
	else :
		targetX = int (frameW / 2)
		targetY = int (frameH / 2)
	cv2.rectangle(frame, (targetX, targetY), (targetX + 2, targetY + 2), (0, 0, 255), 1)

	cv2.imshow("Faces", frame)

	if cv2.waitKey(1) != -1:
		break


video_capture.release()
cv2.destroyAllWindows()
