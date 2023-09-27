import cv2

#reading an image
img = cv2.imread('Picture1.png')
#resizing the image and storing it in a new variable
resized_img = cv2.resize(img,(256,256))
#showing the image in a new window
cv2.imshow("image",resized_img)
#this functions is used so that the window that displays the image is not crossed as soon as it is displayed
cv2.waitKey(0)
#this will destroy the window in which the iamge was openned
cv2.destroyAllWindows()
cv2.imwrite("Picture2.png",resized_img)
