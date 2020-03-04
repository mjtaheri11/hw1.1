import cv2
import numpy as np

def invert(img):
    img = 255 - img
    return img

img = cv2.imread('4.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img1 = invert(gray)
_,thresh = cv2.threshold(img1, 190, 255, cv2.THRESH_BINARY)
kernel1 = thresh[310:334, 80:117]
kernel = kernel1 / np.sum(kernel1[:])
filter_image = cv2.filter2D(thresh, -1, kernel)
_,thresh2 = cv2.threshold(filter_image, 90, 255, cv2.THRESH_BINARY)
filter_image_1 = cv2.filter2D(thresh2, -1, kernel)

cv2.imshow('page', filter_image)
cv2.imshow('thresh2', filter_image_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
