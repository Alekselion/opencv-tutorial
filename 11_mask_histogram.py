import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/test_image.jpg")

# ############# for beautiful output #############
c = 0.5
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

cv2.imshow("original", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# mask
canvas = np.zeros(img.shape[:2], "uint8")
circle = cv2.circle(canvas.copy(), (img.shape[1] // 2 + 20, img.shape[0] // 2 - 70), 50, 255, -1)
mask = cv2.bitwise_and(gray, gray, mask=circle)
cv2.imshow("Mask", mask)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# histogram
canvas = np.zeros(img.shape[:2], "uint8")
circle = cv2.circle(canvas.copy(), (img.shape[1] // 2 + 20, img.shape[0] // 2 - 70), 50, 255, -1)
mask = cv2.bitwise_and(gray, gray, mask=circle)

# gray histogram
plt.figure()
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.xlim([0, 256])

gray_hist = cv2.calcHist([gray], [0], mask, [256], [0, 256])
plt.title("Grayscale histogram")
plt.plot(gray_hist)
plt.show()

# color histogram
plt.figure()
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.xlim([0, 256])

colors = ("b", "g", "r")
for x, col in enumerate(colors):
    hist = cv2.calcHist([img], [x], mask, [256], [0, 256])
    plt.plot(hist, color=col)

plt.title("Color histogram")
plt.show()

# beautiful output
cv2.imshow("Original image and Mask", cv2.hconcat([img, mask]))
cv2.waitKey(0)
cv2.destroyAllWindows()