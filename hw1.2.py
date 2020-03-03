import cv2


def nothing(x):
    pass


img = cv2.imread('space.jpg')
rows, cols, he = img.shape
cv2.namedWindow('image')
cv2.createTrackbar('test', 'image', 0, 360, nothing)

while True:

    k = cv2.waitKey(1) & 0xFF
    if k == ord('e'):
        break

    x = cv2.getTrackbarPos('test', 'image')
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), x, 1)
    rotated_img = cv2.warpAffine(img, M, (cols, rows))
    cv2.imshow('image', rotated_img)
    # k = cv2.waitKey(0)
    # if k == ord('e'):  # wait for 'e' key to exit
    #     cv2.destroyAllWindows()

k = cv2.waitKey(0)
if k == ord('e'):  # wait for 'e' key to exit
    cv2.destroyAllWindows()

# num_rows, num_cols = img.shape[:2]
# cv2.namedWindow('frame')
# rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 0, 1)
# cv2.waitKey(0)
# cv2.imshow('frame', img_rotation)
# img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))
