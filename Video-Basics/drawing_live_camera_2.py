import cv2

# Global Variables
pt1 = (0, 0)
pt2 = (0, 0)
top_left_clicked = False
bottom_right_clicked = False


# Callback Function Rectangle
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, top_left_clicked, bottom_right_clicked

    # Create the callback function for the Mouse Click
    if event == cv2.EVENT_LBUTTONDOWN:
        # Reset the rectangle (it checks if the rectangle has been drawn)
        if top_left_clicked and bottom_right_clicked:
            pt1 = (0, 0)
            pt2 = (0, 0)
            top_left_clicked = False
            bottom_right_clicked = False

        if top_left_clicked == False:
            pt1 = (x, y)
            top_left_clicked = True
        elif bottom_right_clicked == False:
            pt2 = (x, y)
            bottom_right_clicked = True


# Connect to the callback
cap = cv2.VideoCapture(0)

cv2.namedWindow("Test")
cv2.setMouseCallback("Test", draw_rectangle)

while True:
    ret, frame = cap.read()

    # Drawing on Frame Based off of Global Values
    if top_left_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if top_left_clicked and bottom_right_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)

    # Show the frame
    cv2.imshow("Test", frame)

    # Wait for key press to exit window
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
