import cv2

cap = cv2.VideoCapture(0)

while True:
    # capture frame-by-frame
    ret, frame = cap.read()