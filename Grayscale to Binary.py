import cv2

# Read a grayscale image
im_gray = cv2.imread('bunga.jpg', cv2.IMREAD_GRAYSCALE)

# Convert grayscale image to binary
(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 128
im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]

# Show to screen 
cv2.imshow('Grayscale to Binary', im_bw)
cv2.waitKey()
