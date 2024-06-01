import cv2 as cv

citra = cv.imread('bunga.jpg')

citraNOT =  cv.bitwise_not(citra)

cv.imshow('Citra Asli', citra)
cv.imshow('Citra NOT', citraNOT)
cv.waitKey(0)