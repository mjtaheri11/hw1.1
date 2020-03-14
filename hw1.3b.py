import cv2
import numpy as np

k1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
k2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        frame1 = cv2.Canny(frame, 100, 200)
        img_sobelx = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)
        img_sobely = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=5)
        frame2 = img_sobelx + img_sobely
        frame3 = cv2.filter2D(frame, -1, k2)
        frame4 = cv2.filter2D(frame, -1, k1)
        cv2.imshow('frame', frame4)
        out.write(frame4)
        #cv2.imshow('frame', frame1)
        #out.write(frame1)
        #cv2.imshow('frame', frame2)
        #out.write(frame2)
        #cv2.imshow('frame', frame3)
        #out.write(frame3)
        key = cv2.waitKey(27)
        if key == ord('q'):
            break
        # elif key == ord('s'):
        #     out.write(frame)
    else:
        break
