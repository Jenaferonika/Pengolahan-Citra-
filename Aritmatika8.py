import cv2
import numpy as np

# Baca dua citra
img1 = cv2.imread('bunga.jpg')
img2 = cv2.imread('gs_image.png')

# Pastikan kedua citra telah terbaca dengan baik
if img1 is None or img2 is None:
    print("Gagal membaca salah satu atau kedua citra")
else:
    # Pastikan kedua citra memiliki ukuran yang sama
    if img1.shape == img2.shape:
        # Lakukan operasi penambahan citra
        hasil = cv2.add(img1, img2)

        # Menampilkan kedua citra asli dan citra hasil penambahan
        cv2.imshow("Citra Pertama", img1)
        cv2.imshow("Citra Kedua", img2)
        cv2.imshow("Hasil Penambahan", hasil)

        # Menunggu sampai pengguna menekan tombol keyboard dan kemudian menutup jendela citra
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Ukuran kedua citra berbeda, operasi penambahan tidak bisa dilakukan")
