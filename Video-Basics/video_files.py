import cv2
import time

cap = cv2.VideoCapture('./Video-Basics/video_out.mp4')

if cap.isOpened() == False:
    print('ERROR: File not found or wrong codec used!')

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        # Show Video at same rate as it was recorded (20fps)
        time.sleep(1 / 20)
        cv2.imshow('frame', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        break