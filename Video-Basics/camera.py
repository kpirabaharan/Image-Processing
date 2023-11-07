import cv2

cap = cv2.VideoCapture(0)

# Get the width and height of frame
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Video Writer Docs
# https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html

writer = cv2.VideoWriter(
    "./Video-Basics/video_out.mp4",
    cv2.VideoWriter_fourcc(*"MJPG"),
    20,
    (int(width), int(height)),
)

while True:
    ret, frame = cap.read()

    # Write the frame
    writer.write(frame)

    # Convert frame to grayscale
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Show the frame
    cv2.imshow("frame", frame)

    # Wait for key press to exit window
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()
