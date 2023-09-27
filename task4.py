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

#saving the semgmented image
cv2.imwrite('segmented_coins.png',filtered)

# Load the segmented image 
segmented_image = cv2.imread('segmented_coins.png', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if segmented_image is None:
    print("Error: Could not load the image.")
else:
    # Find contours in the segmented image
    contours, _ = cv2.findContours(segmented_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    coin_count = 0

    # Loop through the detected contours
    for contour in contours:
        # Check if the contour is large enough to be considered a coin
        if cv2.contourArea(contour) > 100: 
            coin_count += 1

# Display the segmented image with contours 
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print the number of coins detected
print(f'Number of coins: {coin_count}')
