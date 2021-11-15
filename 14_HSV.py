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

# create track bars
cv2.namedWindow("Track bars")
cv2.resizeWindow("Track bars", 640, 240)

# hue (оттенок)
cv2.createTrackbar("minH", "Track bars", 0, 179, (lambda a: None))
cv2.createTrackbar("maxH", "Track bars", 179, 179, (lambda a: None))

# saturation (насыщенность)
cv2.createTrackbar("minS", "Track bars", 0, 255, (lambda a: None))
cv2.createTrackbar("maxS", "Track bars", 255, 255, (lambda a: None))

# value (яркость)
cv2.createTrackbar("minV", "Track bars", 0, 255, (lambda a: None))
cv2.createTrackbar("maxV", "Track bars", 255, 255, (lambda a: None))

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
while True:
    h_min = cv2.getTrackbarPos("minH", "Track bars")  # min value of HUE
    h_max = cv2.getTrackbarPos("maxH", "Track bars")  # max value of HUE
    s_min = cv2.getTrackbarPos("minS", "Track bars")  # min value of SATURATION
    s_max = cv2.getTrackbarPos("maxS", "Track bars")  # max value of SATURATION
    v_min = cv2.getTrackbarPos("minV", "Track bars")  # min value of VALUE
    v_max = cv2.getTrackbarPos("maxV", "Track bars")  # max value of VALUE
    
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(hsv, lower, upper)
    tune = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
    cv2.imshow("Tune and Mask", cv2.hconcat([tune, mask]))

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()