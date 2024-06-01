import cv2
image = cv2.imread('Disney Princess, lily Z.jpg')

# Periksa apakah citra berhasil dibaca
if image is not None:
    # Dapatkan dimensi citra (lebar x tinggi)
    height, width, _ = image.shape

    x = int(input("Masukkan koordinat x: "))
    y = int(input("Masukkan koordinat y: "))

    pixel_value = image[y, x]  # Perhatikan bahwa y dan x dibalik karena array NumPy memiliki urutan (baris, kolom)
    print(f"Pixel di ({x}, {y}): {pixel_value}")

    box_size = 10  # Ukuran kotak (dalam piksel)
    color = (0, 255, 0)  # Warna kotak (dalam format BGR)
    thickness = 2  # Ketebalan garis kotak

    top_left = (x - box_size, y - box_size)
    bottom_right = (x + box_size, y + box_size)

    highlighted_image = cv2.rectangle(image.copy(), top_left, bottom_right, color, thickness)

    cv2.imshow('Highlighted Image', highlighted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Gagal membaca citra.")
