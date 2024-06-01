import cv2 as cv

citra = cv.imread('gambar apel.jpeg')
citra2 = cv.imread('apel 2.jpeg')

citraXOR =  cv.bitwise_xor(citra, citra2)

cv.imshow('Citra Asli 1', citra)
cv.imshow('Citra Asli 2', citra2)
cv.imshow('Citra XOR', citraXOR)
cv.waitKey(0)