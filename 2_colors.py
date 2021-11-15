import os
import cv2

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/test_image.jpg")

# ############# for beautiful output #############
c = 0.5
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

cv2.imshow("Original image", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# colors
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray)
cv2.waitKey(3000)
cv2.destroyAllWindows()

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image", hsv)
cv2.waitKey(3000)
cv2.destroyAllWindows()

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB image", lab)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# split and merge
b, g, r = cv2.split(img)
bgr = cv2.merge([b, g, r])
cv2.imshow("Red color", r)
cv2.waitKey(3000)
cv2.destroyAllWindows()

cv2.imshow("Green color", g)
cv2.waitKey(3000)
cv2.destroyAllWindows()

cv2.imshow("Blue color", b)
cv2.waitKey(3000)
cv2.destroyAllWindows()

cv2.imshow("Megre blue, green and red images", bgr)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
b = cv2.cvtColor(b, cv2.COLOR_GRAY2BGR)
g = cv2.cvtColor(g, cv2.COLOR_GRAY2BGR)
r = cv2.cvtColor(r, cv2.COLOR_GRAY2BGR)
cv2.imshow("Change colors", cv2.vconcat([
    cv2.hconcat([img, gray, hsv, lab]),
    cv2.hconcat([b, g, r, bgr])
]))
cv2.waitKey(0)
cv2.destroyAllWindows()