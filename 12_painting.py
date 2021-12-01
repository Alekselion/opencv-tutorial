import cv2
import numpy as np

# create canvas
w, h = 300, 350
canvas = np.zeros((h, w, 3), np.uint8)
canvas[:30, :, :] = (150, 150, 150)  # add title to canvas
cv2.putText(canvas, "Status: wait", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 250, 250), 2)
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
        canvas[:30, :, :] = (150, 150, 150)  # clear title
        cv2.putText(canvas, "Status: drawing", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 250, 250), 2)  # change status

    # wait
    if event != cv2.EVENT_MOUSEMOVE:
        canvas[:30, :, :] = (150, 150, 150)  # clear title
        cv2.putText(canvas, "Status: wait", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 250, 250), 2)  # change status

    # clear
    if not flag and event == cv2.EVENT_RBUTTONDOWN:  # left mouse button is release and 
                                                     # right mouse button is press
        canvas[30:, :, :] = (0, 0, 0)  # clear canvas
        canvas[:30, :, :] = (150, 150, 150)  # clear title
        cv2.putText(canvas, "Status: cleared", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (250, 250, 250), 2)  # change status

    
cv2.namedWindow("canvas")  
cv2.setMouseCallback("canvas", drawCircle)  # pass events and mouse coordinates to function => clear
while True:
    cv2.imshow("canvas", canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):  
        break

cv2.destroyAllWindows()  