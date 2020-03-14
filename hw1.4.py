import cv2
import numpy as np

img = cv2.imread('1.jpg')
img1 = cv2.imread('2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray, (3, 3), 0)
img_gaussian1 = cv2.GaussianBlur(gray1, (3, 3), 0)

img_canny = cv2.Canny(img, 100, 200)
img_canny1 = cv2.Canny(img1, 100, 200)

img_sobelx = cv2.Sobel(img_gaussian, cv2.CV_8U, 1, 0, ksize=5)
img_sobely = cv2.Sobel(img_gaussian, cv2.CV_8U, 0, 1, ksize=5)
img_sobel = img_sobelx + img_sobely

img_sobelx1 = cv2.Sobel(img_gaussian1, cv2.CV_8U, 1, 0, ksize=5)
img_sobely1 = cv2.Sobel(img_gaussian1, cv2.CV_8U, 0, 1, ksize=5)
img_sobel1 = img_sobelx1 + img_sobely1

laplacian = cv2.Laplacian(img_gaussian, cv2.CV_64F)
laplacian1 = cv2.Laplacian(img_gaussian1, cv2.CV_64F)

cv2.imshow("1 Image", img)
cv2.imshow("Canny", img_canny)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow('laplacian', laplacian)

cv2.waitKey(0)

cv2.imshow("2 Image", img1)
cv2.imshow("Canny", img_canny1)
cv2.imshow("Sobel X", img_sobelx1)
cv2.imshow("Sobel Y", img_sobely1)
cv2.imshow("Sobel", img_sobel1)
cv2.imshow('laplacian', laplacian1)

# cv2.imshow("Prewitt X", img_prewittx)
# cv2.imshow("Prewitt Y", img_prewitty)
# cv2.imshow("Prewitt", img_prewittx + img_prewitty)

cv2.waitKey(0)
cv2.destroyAllWindows()
