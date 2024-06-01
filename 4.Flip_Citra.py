import cv2 as cv

citra = cv.imread('gambar apel.jpeg')
cv.imshow("Citra Awal", citra) #Menampilkan gambar

#FLIP
flip_horizontal = cv.flip(citra, 1)
flip_vertikal = cv.flip(citra, 90)
flip_Ver_Hor = cv.flip(citra, -1)
cv.imshow("Flip Horizontal", flip_horizontal)
cv.imshow("Flip Vertikal", flip_vertikal)
cv.imshow("Flip Vertikal Horizontal", flip_Ver_Hor)
cv.waitKey(0)