import cv2

def scale_image(image_path, scale_factor):
    # Baca citra dari file
    image = cv2.imread(image_path)

    # Mendapatkan tinggi dan lebar citra
    height, width = image.shape[:2]

    # Menentukan ukuran baru sesuai dengan faktor skala
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Menggunakan metode resize untuk melakukan scaling
    scaled_image = cv2.resize(image, (new_width, new_height))

    return scaled_image

# Path file citra dan faktor skala
image_path = 'Disney Princess, lily Z.jpg'
scale_factor = 2 # Ganti dengan faktor skala yang diinginkan

# Melakukan scaling
scaled_image = scale_image(image_path, scale_factor)

# Menampilkan citra asli
cv2.imshow('Original Image', cv2.imread(image_path))

# Menampilkan citra hasil scaling
cv2.imshow('Scaled Image', scaled_image)

# Menunggu hingga pengguna menekan tombol apa pun
cv2.waitKey(0)

# Menutup semua jendela
cv2.destroyAllWindows()
