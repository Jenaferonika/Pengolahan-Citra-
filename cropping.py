import cv2

def crop_image(image_path, x, y, width, height):
    # Baca citra dari file
    image = cv2.imread(image_path)

    # Melakukan cropping sesuai dengan koordinat dan ukuran yang diberikan
    cropped_image = image[y:y+height, x:x+width]

    return cropped_image

# Path file citra dan koordinat serta ukuran cropping
image_path = 'bunga.jpg'
x = 90  # Koordinat x awal cropping
y = 75   # Koordinat y awal cropping
width = 200  # Lebar cropping
height = 150  # Tinggi cropping

# Melakukan cropping
cropped_image = crop_image(image_path, x, y, width, height)

# Menampilkan citra asli
cv2.imshow('Original Image', cv2.imread(image_path))

# Menampilkan citra hasil cropping
cv2.imshow('Cropped Image', cropped_image)

# Menunggu hingga pengguna menekan tombol apa pun
cv2.waitKey(0)

# Menutup semua jendela
cv2.destroyAllWindows()
