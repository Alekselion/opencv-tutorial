import os
import cv2
import numpy as np
from PIL import ImageGrab

pth = os.path.join(os.getcwd(), "data")

# read image
img = cv2.imread(pth + "/test_image.jpg")
img_gray = cv2.imread(pth + "/test_image.jpg", 0)  # grayscale

# show image
cv2.imshow("Original image", img)
cv2.imshow("Grayscale image", img_gray)
cv2.waitKey(3000)  # wait 3 sec.
cv2.destroyAllWindows()  # destroy windows

# save image
print(f"Before\n{os.listdir(pth)}")
saveImg = cv2.imwrite(pth + "/saved_test_image.jpg", img)
print(f"After\n{os.listdir(pth)}")

# video capture
cap = cv2.VideoCapture(pth + "/test_video.mp4")
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# video save options
out = cv2.VideoWriter(pth + "/saved_test_video.mp4", fourcc, 20.0, (640,480)) 
print(f"Before\n{os.listdir(pth)}")

# read video
while cap.isOpened():
    success, frame = cap.read()
    if success:
        out.write(frame)  # save video
        cv2.imshow("From file.mp4", frame)  # show video
        if cv2.waitKey(20) & 0xFF == ord("q"):  # press 'q' to exit
            break
    else:
        break

print(f"After\n{os.listdir(pth)}")
cap.release()  
out.release() 
cv2.destroyAllWindows()

# get screen
def captureScreen(bbox=(100, 100, 900, 600)):
    capScr = np.array(ImageGrab.grab(bbox))
    capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
    return capScr


# read screen
while True:
    timer = cv2.getTickCount()
    img = captureScreen()
    cv2.imshow("From screen", img)  # show screen
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

# camera setup
cap = cv2.VideoCapture(0)  # id 0 = camera (web)
cap.set(3, 350)  # id 3 = width
cap.set(4, 400)  # id 4 = height
cap.set(10, 1)  # id 10 = bright

# read camera
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # flip (horizontal)
    cv2.imshow("From camera", img)  # show camera
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()