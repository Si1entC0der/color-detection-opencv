import numpy as np
import cv2

def get_limits(color):
    # Convert BGR to HSV
    color_bgr = np.uint8([[color]])
    color_hsv = cv2.cvtColor(color_bgr, cv2.COLOR_BGR2HSV)
    hue = color_hsv[0][0][0]

    delta = 10  # range around hue
    lower = np.array([max(hue - delta, 0), 100, 100], dtype=np.uint8)
    upper = np.array([min(hue + delta, 179), 255, 255], dtype=np.uint8)

    return lower, upper
