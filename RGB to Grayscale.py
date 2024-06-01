#RGB to Grayscale

import cv2

# Read image and convert to grayscale
imgPhoto = cv2.imread('bunga.jpg', cv2.IMREAD_GRAYSCALE)

# Show to screen
cv2.imshow('Hasil Citra RGB Menjadi Citra Gray', imgPhoto)
cv2.waitKey()

# Save to disk
#cv2.imwrite('gs_image.png', image_show)