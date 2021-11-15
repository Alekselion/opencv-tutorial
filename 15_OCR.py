import os
import cv2
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/text.jpg")

# ############# for beautiful output #############
c = 0.4
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

cv2.imshow("Original image", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

height, width = img.shape[:2]

# chapters recognition
chapters = img.copy()
boxes = pt.image_to_boxes(chapters)
for b in boxes.splitlines():
    b = b.split(" ")
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(chapters, (x, height-y), (w, height-h), (0, 255, 0), 1)
    cv2.putText(chapters, b[0], (x, height-y+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

cv2.imshow("Recognized characters", chapters)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# digits recognition
only_digit = r"--oem 3 --psm 6 outputbase digits"
digits = img.copy()
boxes = pt.image_to_boxes(digits, config=only_digit)
for b in boxes.splitlines():
    b = b.split(" ")
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(digits, (x, height-y), (w, height-h), (0, 255, 0), 1)
    cv2.putText(digits, b[0], (x, height-y+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

cv2.imshow("Recognized digits", digits)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# words recognition
words = img.copy()
boxes = pt.image_to_data(words)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv2.rectangle(words, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cv2.putText(words, b[11], (x, y+h+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255), 1)

cv2.imshow("Recognized words", words)
cv2.waitKey(3000)
cv2.destroyAllWindows()

# beautiful output
cv2.imshow("Optical Character Recognition", cv2.hconcat([
    cv2.hconcat([img, chapters]),
    cv2.hconcat([digits, words])
]))
cv2.waitKey(0)
cv2.destroyAllWindows()