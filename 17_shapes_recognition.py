import os
import cv2

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/shapes.png")

# ############# for beautiful output #############
c = 0.6
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

cv2.imshow("Original image", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

shapes = img.copy()

# find contours
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 1)
canny = cv2.Canny(blur, 50, 50)
contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow("Found contours", canny)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# detect shapes
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:
        perimeter = cv2.arcLength(cnt, closed=True)
        angle = cv2.approxPolyDP(cnt, epsilon=0.03 * perimeter, closed=True)
        cv2.drawContours(shapes, cnt, -1, (255, 0, 0), 4)
        
        # make borders
        x, y, w, h = cv2.boundingRect(angle)
        cv2.rectangle(shapes, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # recognize shape
        if len(angle) == 3:
            name = "triangle"
        elif len(angle) == 4:
            aspect_ratio = w / float(h)
            if 0.95 < aspect_ratio < 1.05:
                name = "square"
            else:
                name = "rectangle"
        elif len(angle) == 5:
            name = "pentagon"
        elif len(angle) == 6:
            name = "hexagon"
        elif len(angle) == 7:
            name = "heptagon"
        elif len(angle) > 7:
            name = "circle"
        else:
            name = "ellipse"

        cv2.putText(shapes, name, (x + (w // 2) - 30, y + h + 11), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)

cv2.imshow("Recognized shapes", shapes)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Recognized shapes", cv2.hconcat([img, shapes]))
cv2.waitKey(0)
cv2.destroyAllWindows()