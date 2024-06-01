import cv2 as cv
import numpy as np

citra = cv.imread('gambar apel.jpeg')

gray = cv.cvtColor(citra, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra Grayscale', gray)
cv.imshow('Citra Biner', thresh)
cv.imshow('Citra Opening', opening)

cv.waitKey(0)
cv.destroyAllWindows()