import cv2
import numpy as np

img = cv2.imread('limbo.png', 0)
kernel = np.ones((5, 5), np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
img_dilation = cv2.dilate(img, kernel, iterations=20)
img_erosion = cv2.erode(img, kernel, iterations=20)

cv2.imshow("opening", opening)
cv2.imshow('closing', closing)
cv2.imshow('Dilation', img_dilation)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Input', img)

cv2.waitKey(0)
