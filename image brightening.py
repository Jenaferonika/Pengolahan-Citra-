import cv2
import numpy as np

# Baca citra dari file
image = cv2.imread('bunga.jpg')

# Periksa apakah citra berhasil dibaca
if image is not None:
    # Definisikan faktor brightening (misalnya, 1.5 untuk meningkatkan kecerahan)
    brightening_factor = 1.5

    # Lakukan brightening pada citra
    brightened_image = np.clip(image * brightening_factor, 0, 255).astype(np.uint8)

    cv2.imshow("Citra Asli", image)
    cv2.imshow("Citra Brightened", brightened_image)

    # Tunggu sampai pengguna menekan tombol apa saja
    cv2.waitKey(0)

    # Tutup jendela setelah tombol ditekan
    cv2.destroyAllWindows()
else:
    print("Citra tidak dapat dibaca")
