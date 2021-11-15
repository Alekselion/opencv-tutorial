import os
import cv2

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

# threshold
etval, threshold = cv2.threshold(gray, 50, 230, cv2.THRESH_BINARY)  # pixel < 160 = 0, pixel > 230 = 1
threshold = cv2.cvtColor(threshold, cv2.COLOR_GRAY2BGR)
cv2.imshow("Threshold", threshold)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# adaptive threshold
adapt_threshold = cv2.adaptiveThreshold(gray, 200,  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 13)
adapt_threshold = cv2.cvtColor(adapt_threshold, cv2.COLOR_GRAY2BGR)
cv2.imshow("Adaptive threshold", adapt_threshold)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# contours with treshold
_, thresh = cv2.threshold(gray, 50, 230, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
result1 = cv2.drawContours(img.copy(), contours, -1, (200, 50, 50), 2)
cv2.imshow("Contours threshold", result1)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# contours with adaptive treshold
thresh_adapt = cv2.adaptiveThreshold(gray, 230, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 13)
contours, _ = cv2.findContours(thresh_adapt, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
result2 = cv2.drawContours(img.copy(), contours, -1, (200, 50, 50), 2)
cv2.imshow("Contours adaptive threshold", result2)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# contours with canny
edges = cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (5, 5), 0), 50, 80)
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
result3 = cv2.drawContours(img.copy(), contours, -1, (200, 50, 50), 2)
cv2.imshow("Contours canny", result3)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Threshold and Contours", cv2.vconcat([
    cv2.hconcat([img, threshold, adapt_threshold]),
    cv2.hconcat([result3, result1, result2])
]))
cv2.waitKey(0)
cv2.destroyAllWindows()