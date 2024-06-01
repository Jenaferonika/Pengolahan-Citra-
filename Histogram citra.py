import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca citra
citra = cv2.imread('bunga.jpg', cv2.IMREAD_GRAYSCALE)

# Menghitung histogram
histogram = cv2.calcHist([citra], [0], None, [256], [0, 256])

# Menampilkan gambar asli
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.imshow(citra, cmap='gray')
plt.title("Gambar Asli")
plt.axis('off')

# Menampilkan histogram
plt.subplot(1, 2, 2)
plt.plot(histogram, color='black')
plt.title("Histogram Citra")
plt.xlabel("Intensitas Piksel")
plt.ylabel("Jumlah Piksel")
plt.xlim([0, 256])
plt.grid(True)

# Menampilkan gambar histogram
plt.tight_layout()
plt.show()
