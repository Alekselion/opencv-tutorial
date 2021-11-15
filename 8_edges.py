import os
import cv2
import numpy as np

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

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# laplacian
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
cv2.imshow("Method 'Laplacian'", laplacian)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# sobel
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sobel = cv2.bitwise_or(sobelx, sobely)
cv2.imshow("Method 'Sobel'", sobel)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# canny
canny = cv2.Canny(img, 100, 200)
cv2.imshow("Method 'Canny'", canny)
cv2.waitKey(3000)
cv2.destroyAllWindows()