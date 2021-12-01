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

constant = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_CONSTANT,value=[0, 255, 0]) 
cv2.imshow("Border constant", constant)
cv2.waitKey(3000)
cv2.destroyAllWindows()

wrap = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_WRAP)
cv2.imshow("Border wrap", wrap)
cv2.waitKey(3000)
cv2.destroyAllWindows()

replicate = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_REPLICATE)
cv2.imshow("Border replicate", replicate)
cv2.waitKey(3000)
cv2.destroyAllWindows()

reflect = cv2.copyMakeBorder(img, 40, 40, 40, 40, cv2.BORDER_REFLECT)
cv2.imshow("Border reflect", reflect)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Borders", cv2.vconcat([
    cv2.hconcat([constant, wrap]),
    cv2.hconcat([replicate, reflect])
]))
cv2.waitKey(0)
cv2.destroyAllWindows()