import os
import cv2
import numpy as np
from pyzbar.pyzbar import decode

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/qrcodes.jpg")

# ############# for beautiful output #############
c = 0.4
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

cv2.imshow("Original image", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

result = img.copy()
for barcode in decode(result):
    text = barcode.data.decode("utf-8")
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(result, [pts], True, (0, 0, 255), 5)
    pts2 = barcode.rect
    cv2.putText(result, text, (pts2[0]-10, pts2[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)

cv2.imshow("Read QR-code", result)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("QR-code reader", cv2.hconcat([img, result]))
cv2.waitKey(0)
cv2.destroyAllWindows()