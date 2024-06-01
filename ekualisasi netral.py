import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca citra dalam mode warna (RGB)
citra = cv2.imread("bunga.jpg")

# Memisahkan kanal warna
kanal_biru, kanal_hijau, kanal_merah = cv2.split(citra)

# Menghitung histogram untuk setiap kanal
histogram_biru = cv2.calcHist([kanal_biru], [0], None, [256], [0, 256])
histogram_hijau = cv2.calcHist([kanal_hijau], [0], None, [256], [0, 256])
histogram_merah = cv2.calcHist([kanal_merah], [0], None, [256], [0, 256])

# Melakukan ekualisasi citra pada setiap kanal
ekual_biru = cv2.equalizeHist(kanal_biru)
ekual_hijau = cv2.equalizeHist(kanal_hijau)
ekual_merah = cv2.equalizeHist(kanal_merah)

# Menggabungkan kembali kanal-kanal yang telah diekualisasi
citra_ekual = cv2.merge((ekual_biru, ekual_hijau, ekual_merah))

# Menampilkan citra asli dan citra hasil ekualisasi
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(citra, cv2.COLOR_BGR2RGB))
plt.title("Citra Asli")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(citra_ekual, cv2.COLOR_BGR2RGB))
plt.title("Citra Hasil Ekualisasi")
plt.axis('off')

plt.tight_layout()
plt.show()
