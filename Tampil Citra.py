import cv2

# Baca citra dari file
image = cv2.imread('bunga.jpg')

# Periksa apakah citra berhasil dibaca
if image is not None:
    # Tampilkan citra dalam jendela
    cv2.imshow('bunga.jpg', image)
    # Tunggu sampai pengguna menekan tombol apa saja
    cv2.waitKey(0)
    # Tutup jendela setelah tombol ditekan
    cv2.destroyAllWindows()
else:
    print("Citra tidak dapat dibaca")
