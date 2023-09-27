import cv2
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
import numpy as np

def filter_image(image, mask):
    r = image[:,:,0] * mask
    g = image[:,:,1] * mask
    b = image[:,:,2] * mask

    return np.dstack([r,g,b])

img1 = cv2.imread("Picture2.png")
#converting the image to RGB format
img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
#converting to gray image
gray_img = cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
#applying threshold
threshold = threshold_otsu(gray_img)
#creating mask
img_otsu = gray_img < threshold
#applying mask
filtered = filter_image(img2, img_otsu)
#displaying the final image
cv2.imshow("Img",filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()