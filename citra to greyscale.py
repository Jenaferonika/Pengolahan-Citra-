import cv2

# Read the original image
imgRGB = cv2.imread('bunga.jpg')

# Convert the image to grayscale
imgGray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)

# Show the original and grayscale images
cv2.imshow('Citra Asli', imgRGB)
cv2.imshow('Citra Grayscale', imgGray)

# Wait for a key event and close windows when any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the grayscale image to disk
cv2.imwrite('gs_image.png', imgGray)
