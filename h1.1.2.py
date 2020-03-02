import cv2

img = cv2.imread('football.jpg')
img1 = img
recball = cv2.rectangle(img, (300, 460), (375, 530), (0, 255, 0), 2)
cv2.imshow("balldetector", recball)
cv2.waitKey(0)
#cv2.imshow('image', img)
ball = img1[460:530, 300:380]
img1[460:530, 600:680] = ball
cv2.imshow("image", img1)
cv2.waitKey(0)