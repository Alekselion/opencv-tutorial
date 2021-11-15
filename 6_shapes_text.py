import cv2
import numpy as np

canvas = np.zeros((600, 600, 3), dtype="uint8")  # (height, width, channel)
h, w = canvas.shape[:2]
cv2.imshow("Blank canvas", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()

canvas[:100, :w // 4] = 255, 0, 0  # blue
canvas[100:200, :w // 2] = 0, 255, 0  # green
canvas[200:300, :] = 0, 0, 255  # red
cv2.imshow("Partial image coloring", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# rectangle
cv2.rectangle(canvas, pt1=(10, h // 2 + 10), pt2=(110, h // 2 + 110), color=(0, 0, 255), thickness=2)
cv2.rectangle(canvas, (10, h // 2 + 120), (110, h // 2 + 220), (0, 0, 255), -1)  # -1 = закрасить
cv2.imshow("Draw rectangle", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# circle
cv2.circle(canvas, center=(170, h // 2 + 60), radius=50, color=(255, 0, 0), thickness=2)
cv2.circle(canvas, (170, h // 2 + 170), 50, (255, 0, 0), -1)
cv2.imshow("Draw circle", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# line
cv2.line(canvas, pt1=(240, h // 2 + 110), pt2=(350, h // 2 + 10), color=(0, 255, 0), thickness=3)
cv2.line(canvas, (240, h // 2 + 170), (350, h // 2 + 170), (0, 255, 0), 5)
cv2.imshow("Draw line", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# ellipse
cv2.ellipse(canvas, (450, h // 2 + 60), (40, 60), 5, 0, 360, (255, 255, 0), 0)
cv2.ellipse(canvas, (450, h // 2 + 170), (60, 40), 5, 0, 360, (255, 255, 0), -1)
cv2.imshow("Draw ellipse", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# polylines
pts = np.array([[400, 80], [500, 130], [430, 110], [390, 180]], np.int32)  
cv2.polylines(canvas, [pts], True, (0,255,255), 3)
cv2.imshow("Draw polyline", canvas)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# text
cv2.putText(canvas, "Text text text", org=(10, h - 30), color=(0, 255, 255), thickness=1, 
            fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1)
cv2.imshow("Put text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()