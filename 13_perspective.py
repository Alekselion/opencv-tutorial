import os
import cv2
import numpy as np

pth = os.path.join(os.getcwd(), "data")
img = cv2.imread(pth + "/tv.png")

# ############# for beautiful output #############
c = 0.7
h, w = int(img.shape[0] * c), int(img.shape[1] * c)
img = cv2.resize(img, (w, h))
# ################################################

points = np.zeros((4,2), np.int)
labels = ["topLeft", "topRight", "bottomLeft", "bottomRight"]
counter = 0


def mouse_point(event, x, y, *args):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:  # click
        points[counter] = x, y  # add coordinates
        counter += 1


cp = img.copy()
while True:
    if counter == 4:
        width, height = 300, 200
        # pts1 = np.float32([
        #     points[0],  # top left
        #     points[1],  # top right
        #     points[2],  # bottom left
        #     points[3]  # bottom right
        # ])
        pts1 = np.float32([*points])  # unpack
        pts2 = np.float32([
            [0, 0],
            [width, 0],
            [0, height],
            [width, height]
        ])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(img, matrix, (width, height))
        cv2.imshow("Perspective image", result)
    
    for x in range(4):
        cv2.circle(cp, (points[x,0], points[x,1]), 3, (255, 0, 255), -1)
        cv2.putText(cp, labels[x], (points[x,0] - 40, points[x,1] + 20), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 255), 1)

    cv2.imshow("Original image", cp)
    cv2.setMouseCallback("Original image", mouse_point)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break