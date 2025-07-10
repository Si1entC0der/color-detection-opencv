import cv2
import numpy as np
from util import get_limits

# BGR color for yellow
yellow = [0, 255, 255]

cap = cv2.VideoCapture(0)  # Use 0 unless you know your camera index

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get HSV limits for yellow
    lower, upper = get_limits(yellow)

    # Create mask
    mask = cv2.inRange(hsv, lower, upper)

    # Find contours of the yellow areas
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # ignore small objects
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Detected Frame", frame)
    # cv2.imshow("Yellow Mask", mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



