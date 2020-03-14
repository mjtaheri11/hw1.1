import cv2
import numpy as np

img = cv2.imread('2.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
width = 300
heigth = 400
resized = cv2.resize(img, (heigth, width), interpolation = cv2.INTER_AREA)
#cv2.Canny()
#blur = cv2.GaussianBlur(resized, (5, 5), 0)

k = np.array(np.ones((11, 11), np.float32))/121
k1 = np.array([[-1, -1, -1],[0, 0, 0],[1, 1, 1]])
k2 = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
#_,thresh2 = cv2.threshold(filter_   image, 90, 255, cv2.THRESH_BINARY)
output0 = cv2.filter2D(resized, -1, k)
#_,thresh2 = cv2.threshold(filter_image, 90, 255, cv2.THRESH_BINARY)
output1 = cv2.filter2D(resized, -1, k1)
#_,thresh2 = cv2.threshold(filter_image, 90, 255, cv2.THRESH_BINARY)
output2 = cv2.filter2D(resized, -1, k2)

output = resized.astype(np.float32) - output0.astype(np.float32)
#output = resized = output0
output = output.astype(np.uint8)

cv2.imshow('output', output0)
cv2.imwrite('output.jpg', output0)
cv2.waitKey(0)
cv2.imshow('output', output1)
cv2.imwrite('output0.jpg', output1)
cv2.waitKey(0)
cv2.imshow('output', output2)
cv2.imwrite('output.jpg', output2)
cv2.waitKey(0)
cv2.imshow('output', output)
cv2.waitKey(0)
