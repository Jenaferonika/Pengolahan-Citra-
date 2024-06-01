import cv2 as cv

citra = cv.imread('gambar apel.jpeg')
cv.imshow("citra awal", citra) #Menampilkan gambar

skala_persen = 180
width = int(citra.shape[1] * skala_persen/100)
heigth = int(citra.shape[0] * skala_persen/100)

merged = (width, heigth)

zoom = cv.resize(citra, merged, interpolation = cv.INTER_LINEAR)
print("Zoom: ", zoom.shape)

cv.imshow("Citra Zooming", zoom)

cv.waitKey(0)