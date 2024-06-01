import cv2 as cv

citra = cv.imread('bunga.jpg')
citra2 = cv.imread('gs_image.png')

citraAND =  cv.bitwise_and(citra, citra2)

cv.imshow('Citra Asli 1', citra)
cv.imshow('Citra Asli 2', citra2)
cv.imshow('Citra AND', citraAND)
cv.waitKey(0)