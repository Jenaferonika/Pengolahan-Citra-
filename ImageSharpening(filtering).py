import cv2 as cv
import numpy as np

citra = citra = cv.imread('bunga.jpg')

kernel = np.array([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])

output = cv.filter2D(citra, -1, kernel)

cv.imshow('Gambar Asli', citra)
cv.imshow('Hasil Filtering', output)
cv.waitKey(0)
cv.destroyAllWindows()