import cv2

img = cv2.imread('Picture2.png')
#first we convert the image to gray scale
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#then we convert the gray scale image to binary image
#we apply the threshold for this
ret,thresh_img = cv2.threshold(gray_img,120,255,cv2.THRESH_BINARY)

cv2.imshow("Binary Image",thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()