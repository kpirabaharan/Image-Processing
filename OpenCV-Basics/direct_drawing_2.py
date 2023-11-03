import cv2
import numpy as np

# Variables
drawing = False
ix = -1
iy = -1


# Fn
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)


cv2.namedWindow(winname="drawing")
cv2.setMouseCallback("drawing", draw_rectangle)

# Show Img with OpenCV
img = np.zeros((512, 512, 3))

while True:
    cv2.imshow("drawing", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
