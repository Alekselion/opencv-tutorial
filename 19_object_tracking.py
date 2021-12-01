import os
import cv2

pth = os.path.join(os.getcwd(), "data")
cap = cv2.VideoCapture(pth + "/ball.mp4")
tracker = cv2.TrackerKCF_create()
texts = ["1. Press 's' to select object for tracking.", "2. Select tracking object and press 'enter'."]
while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.putText(frame, texts[0], (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
        cv2.imshow("ROI selector", frame)
        if cv2.waitKey(30) & 0xff == ord("s"):
            cv2.putText(frame, texts[1], (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
            bbox = cv2.selectROI(frame, False)  # select object to track
            success_track = tracker.init(frame, bbox)
            cv2.destroyAllWindows()
            break
    else:
        break

while cap.isOpened():
    success_cap, frame = cap.read()
    if success_cap:
        success_track, bbox = tracker.update(frame)
        cv2.putText(frame, "Status:", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
        if success_track:
            x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 255, 0), 2)
            cv2.putText(frame, "tracking", (85, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 2)
            cv2.putText(frame, "lost", (85, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    
        cv2.imshow("Object tracking", frame) 
        if cv2.waitKey(25) & 0xff == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()