import cv2 as cv
import numpy as np

citra = cv.imread('bunga.jpg')

gray = cv.cvtColor(citra, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

closing = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra Grayscale', gray)
cv.imshow('Citra Biner', thresh)
cv.imshow('Citra Closing', closing)

cv.waitKey(0)
cv.destroyAllWindows()