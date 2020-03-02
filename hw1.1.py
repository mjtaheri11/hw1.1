import cv2

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 100)
fontScale = 1
fontColor = (0, 0, 0)
lineType = 2

cv2.putText(img, '98205849',
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)

cv2.putText(gray, '98205849 ',
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.imshow('image', gray)
k = cv2.waitKey(0)
if k == ord('e'):  # wait for 'e' key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('edited_img.png', img)
    cv2.imwrite('edited_img1.png', gray)
    cv2.destroyAllWindows()
