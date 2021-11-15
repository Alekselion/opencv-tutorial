import os
import cv2

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/test_image.jpg")
cv2.imshow("Original image", img)
cv2.waitKey(3000)

# crop
img_crop = img[50:300, 320:570]
cv2.imshow("Croped image", img_crop)
cv2.waitKey(3000)

# resize
print(f"Image shape before resizing: {img.shape}")
scale = 0.5
width, height = int(img.shape[1] * scale), int(img.shape[0] * scale)
img_resize = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)  
print(f"Image shape after resizing: {img_resize.shape}")
cv2.imshow("Resized image", img_resize)
cv2.waitKey(3000)
cv2.destroyAllWindows()
