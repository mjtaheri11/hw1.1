import cv2
import numpy as np

k1 = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
k2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
out1 = cv2.VideoWriter('outpy1.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
out2 = cv2.VideoWriter('outpy2.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
out3 = cv2.VideoWriter('outpy3.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
out4 = cv2.VideoWriter('outpy4.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        out.write(frame)
        frame1 = cv2.Canny(frame, 100, 200)
        out1.write(frame1)
        img_sobelx = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)
        img_sobely = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=5)
        frame2 = img_sobelx + img_sobely
        out2.write(frame2)
        frame3 = cv2.filter2D(frame, -1, k2)
        out3.write(frame3)
        frame4 = cv2.filter2D(frame, -1, k1)
        out4.write(frame4)
        #   cv2.imshow('frame', frame1)
        # out.write(frame1)
        # cv2.imshow('frame', frame2)
        # out.write(frame2)
        # cv2.imshow('frame', frame3)
        # out.write(frame3)
        key = cv2.waitKey(27)
        if key == ord('q'):
            break
        # elif key == ord('s'):
        #     out.write(frame)
    else:
        break
