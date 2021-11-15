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

# average blur
average_blur = cv2.blur(img, ksize=(5, 5))
cv2.imshow("Average blur", average_blur)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# median blur
median_blur = cv2.medianBlur(img, 5)
cv2.imshow("Median blur", median_blur)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# Gaussian blur
gauss_blur = cv2.GaussianBlur(img, (5, 5), sigmaX=0)
cv2.imshow("Gaussian blur", gauss_blur)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# bilateral blur
bilateral = cv2.bilateralFilter(img, d=10, sigmaColor=75, sigmaSpace=75)
cv2.imshow("Bilateral filter", bilateral)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# box filter
box = cv2.boxFilter(img, 0, (2,1), img, (-1,-1), False, cv2.BORDER_DEFAULT)
cv2.imshow("Box filter", box)
cv2.waitKey(3000)
cv2.destroyAllWindows()

img = cv2.imread(pth + "/test_image.jpg")

# ############# for beautiful output #############
c = 0.5
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

# 2D filter
kernel = np.ones((5,5), np.float32)/25  
twod = cv2.filter2D(img, -1, kernel)
cv2.imshow("Filter 2D", twod)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# dilate filter
kernel = np.ones((5,5), np.uint8)
dialation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Dilate filter", dialation)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# erode filter
eroded = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Erode filter", eroded)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# denoising filter
denois = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
cv2.imshow("Denoising filter", denois)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Filters", cv2.vconcat([
    cv2.hconcat([img, average_blur, median_blur, gauss_blur, bilateral]),
    cv2.hconcat([box, twod, dialation, eroded, denois])
]))
cv2.waitKey(0)
cv2.destroyAllWindows()