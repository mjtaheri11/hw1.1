import cv2
import numpy as np


def nothing(x):
    pass


img = cv2.imread('space.jpg')
img = cv2.resize(img, None, None, .5, .5, interpolation=cv2.INTER_LINEAR)
rows, cols, he = img.shape
cv2.namedWindow('image')
cv2.createTrackbar('test', 'image', 0, 360, nothing)
color = (0, 255, 0)
thickness = 9

while True:

    x = cv2.getTrackbarPos('test', 'image')
    matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), x, .5)
    start_point = (1, 1)
    y = np.matrix('[1; 1; 1]')
    end_point = np.matmul(matrix, y)
    rotated_img = cv2.warpAffine(img, matrix, (cols, rows))
    rotated_img = cv2.resize(rotated_img, None, None, 1, 1, interpolation=cv2.INTER_LINEAR)
    #img = cv2.resize(img, None, None, .5, .5, interpolation=cv2.INTER_LINEAR)
    both = np.hstack((img, rotated_img))
    cv2.line(both, start_point, (int(end_point[0]  + img.shape[1]), int(end_point[1])), color, thickness)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('e'):
        break

    cv2.imshow('image', both)

cv2.destroyAllWindows()
    # k = cv2.waitKey(0)
    # if k == ord('e'):  # wait for 'e' key to exit

# num_rows, num_cols = img.shape[:2]
# cv2.namedWindow('frame')
# rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 0, 1)
# cv2.waitKey(0)
# cv2.imshow('frame', img_rotation)
# img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
