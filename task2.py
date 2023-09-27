import cv2

img = cv2.imread('Picture2.png')
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("grayImage",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()