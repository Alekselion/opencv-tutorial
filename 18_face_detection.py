import os
import cv2

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/faces.jpg")

# ############# for beautiful output #############
c = 0.6
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

cv2.imshow("Original image", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# face detection
faceDetect = img.copy()
gray = cv2.cvtColor(faceDetect, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=3, minNeighbors=5, minSize=(10, 10))
for (x, y, w, h) in faces:
    cv2.rectangle(faceDetect, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(faceDetect, "face", (x+w//2-30, y+5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
cv2.imshow("Faces detected", faceDetect)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# eyes detection
eyesDetect = img.copy()
gray = cv2.cvtColor(eyesDetect, cv2.COLOR_BGR2GRAY)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=3, minNeighbors=5, minSize=(10, 10))
for (ex, ey, ew, eh) in eyes:
    cv2.ellipse(eyesDetect, (ex + ew // 2, ey + eh // 2), (23, 13), 0, 0, 360, (0, 255, 0), 2)
    cv2.putText(eyesDetect, "eye", (ex+ew//2-10, ey+eh), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

cv2.imshow("Eyes detected", eyesDetect)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# blur face
blurFace = img.copy()
gray = cv2.cvtColor(blurFace, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, scaleFactor=3, minNeighbors=5, minSize=(10, 10))
for (x, y, w, h) in faces:
    # find area of face
    face = blurFace[y:y + h, x:x + w]
    height, width = face.shape[:2]
    dw = int(width // 3)
    dh = int(height // 3)
    if dw % 2 == 0:
        dw -= 1
    if dh % 2 == 0:
        dh -= 1

    # blur
    blurFace[y:y + h, x:x + w] = cv2.GaussianBlur(face, (dw, dh), 0)

cv2.imshow("Blurred faces", blurFace)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Faces detected Eyes detected Blurred faces", cv2.vconcat([
    cv2.hconcat([img, faceDetect]),
    cv2.hconcat([eyesDetect, blurFace])
]))
cv2.waitKey(0)
cv2.destroyAllWindows()

