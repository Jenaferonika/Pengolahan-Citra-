import cv2 as cv

citra = cv.imread('gambar apel.jpeg')
citra2 = cv.imread('apel 2.jpeg')

citraOR =  cv.bitwise_or(citra, citra2)

cv.imshow('Citra Asli 1', citra)
cv.imshow('Citra Asli 2', citra2)
cv.imshow('Citra OR', citraOR)
cv.waitKey(0)