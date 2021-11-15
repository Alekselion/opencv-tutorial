import cv2
import numpy as np

flag = False


def drawCircle(event, x, y, flags, param):
    """ left mouse button - draw on canvas
        right mouse button - clear canvas
    """
    global flag
    if event == cv2.EVENT_LBUTTONDOWN:
        flag = True
        cv2.circle(canvas, (x,y), 10, (255, 255, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        flag = False

    # draw
    if flag and event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(canvas, (x,y), 10, (255, 255, 255), -1)

    # clear
    if not flag and event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(canvas, (0, 0), (h, w), (0, 0, 0), -1)


w, h = 300, 350
canvas = np.zeros((h, w, 3), np.uint8)  
cv2.namedWindow("canvas")  
cv2.setMouseCallback("canvas", drawCircle)
while True:  
    cv2.imshow("canvas", canvas)  
    if cv2.waitKey(1) & 0xFF == ord("q"):  
        break

cv2.destroyAllWindows()  