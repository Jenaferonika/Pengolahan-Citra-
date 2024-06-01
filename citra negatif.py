import cv2

# Baca citra dari file
image = cv2.imread('gambar apel.jpeg')

# Periksa apakah citra berhasil dibaca
if image is not None:
    # Mengambil dimensi citra
    height, width, _ = image.shape

    # Invert nilai piksel pada setiap saluran warna
    negative_image = 255 - image

    cv2.imshow('Gambar Asli', image)
    cv2.imshow('Gambar Negatif', negative_image)

    # Tunggu sampai pengguna menekan tombol apa saja
    cv2.waitKey(0)

    # Tutup jendela setelah tombol ditekan
    cv2.destroyAllWindows()
else:
    print("Citra tidak dapat dibaca")
