import cv2
import numpy as np

# create canvas
w, h = 300, 350
canvas = np.zeros((h, w, 3), np.uint8)  
flag = False


def drawCircle(event, x, y, *otherParams):
    """ left mouse button - draw on canvas
        right mouse button - clear canvas
    """
    global flag
    if event == cv2.EVENT_LBUTTONDOWN:  # left mouse button is press
        flag = True
        cv2.circle(canvas, (x,y), 10, (255, 255, 255), -1)  # draw point
    elif event == cv2.EVENT_LBUTTONUP:  # left mouse button is release
        flag = False

    # draw
    if flag and event == cv2.EVENT_MOUSEMOVE:  # left mouse button is press and move mouse 
        cv2.circle(canvas, (x,y), 10, (255, 255, 255), -1)  # draw points

    # clear
    if not flag and event == cv2.EVENT_RBUTTONDOWN:  # left mouse button is release and 
                                                     # right mouse button is press
        canvas[:, :, :] = (0, 0, 0)  # paint canvas black => clear


cv2.namedWindow("canvas")  
cv2.setMouseCallback("canvas", drawCircle)  # pass events and mouse coordinates to function
while True:
    cv2.imshow("canvas", canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):  
        break

cv2.destroyAllWindows()  
