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

# rotate
horizontal = cv2.flip(img, flipCode=1)
cv2.imshow("Horizontal flip", horizontal)
cv2.waitKey(3000)
cv2.destroyAllWindows()

vertical = cv2.flip(img, flipCode=0)
cv2.imshow("Vertical flip", vertical)
cv2.waitKey(3000)
cv2.destroyAllWindows()

conversely = cv2.flip(img, flipCode=-1)
cv2.imshow("Horizontal and vertical flip", conversely)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# image rotation function
def turn(image, angle, center=None):
    height, width = image.shape[:2]
    if center is None:
        center = (width // 2, height // 2)

    rot_matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, rot_matrix, (width, height))


rotated = turn(img, 10, (20, 10))
cv2.imshow("Rotated image", rotated)
cv2.waitKey(3000)
cv2.destroyAllWindows()


# image transformation function
def transform(image, x, y):
    """  x = right
        -x = left
         y = down
        -y = up
    """
    height, width = image.shape[:2]
    matrix = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(image, matrix, (width, height))


transformed = transform(img, -50, 50)
cv2.imshow("Transformaed image", transformed)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Rotate Transform Perspective", cv2.vconcat([
    cv2.hconcat([img, horizontal, rotated]),
    cv2.hconcat([vertical, conversely, transformed])
]))
cv2.waitKey(0)
cv2.destroyAllWindows()