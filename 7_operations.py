import os
import cv2
import numpy as np

pth = os.path.join(os.getcwd(), "data")
img1 = cv2.imread(pth + "/square.jpg")
img2 = cv2.imread(pth + "/circle.jpg")

# ############# for beautiful output #############
c = 0.5
h, w = int(img1.shape[0] * c), int(img1.shape[1] * c)
img1 = cv2.resize(img1, (w, h))

h, w = int(img2.shape[0] * c), int(img2.shape[1] * c)
img2 = cv2.resize(img2, (w, h))
# ################################################

cv2.imshow("Original images", cv2.hconcat([img1, img2]))
cv2.waitKey(3000)
cv2.destroyAllWindows()

# arithmetic operations
img_sum = cv2.add(img1, img2)
cv2.imshow("Image addition", img_sum)
cv2.waitKey(3000)
cv2.destroyAllWindows()

img_dif = cv2.subtract(img2, img1)
cv2.imshow("Subtracting images", img_dif)
cv2.waitKey(3000)
cv2.destroyAllWindows()

superimposition = cv2.addWeighted(img1, 0.5, img2, 0.4, 0)
cv2.imshow("Superimposition images", superimposition)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# bitwise operations
dest_and = cv2.bitwise_and(img1, img2, mask=None)
cv2.imshow("Bitwise AND", dest_and)
cv2.waitKey(3000)
cv2.destroyAllWindows()

dest_or = cv2.bitwise_or(img2, img1, mask=None)
cv2.imshow("Bitwise OR", dest_or)
cv2.waitKey(3000)
cv2.destroyAllWindows()

dest_xor = cv2.bitwise_xor(img2, img1, mask=None)
cv2.imshow("Bitwise XOR", dest_xor)
cv2.waitKey(3000)
cv2.destroyAllWindows()

dest_not = cv2.bitwise_not(img2, mask=None)
cv2.imshow("Bitwise NOT", dest_not)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Arithmetic operations", cv2.hconcat([img_sum, img_dif]))
cv2.imshow("Bitwise operations", cv2.vconcat([
    cv2.hconcat([dest_and, dest_or]),
    cv2.hconcat([dest_xor, dest_not])
]))
cv2.imshow("Superimposition images", superimposition)
cv2.waitKey(0)
cv2.destroyAllWindows()