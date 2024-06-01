import cv2 as cv
import numpy as np

citra = citra = cv.imread('bunga.jpg')

kernel = np.ones((5, 5), np.float32) / 25

output = cv.filter2D(citra, -1, kernel)

cv.imshow('Gambar Asli', citra)
cv.imshow('Hasil Filtering', output)
cv.waitKey(0)
cv.destroyAllWindows()