import cv2
import numpy as np

def translate(image, dx, dy):
    # Mendapatkan ukuran gambar
    rows, cols = image.shape[:2]
    # Membuat matriks translasi
    translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
    # Melakukan translasi gambar
    translated_image = cv2.warpAffine(image, translation_matrix, (cols, rows))
    return translated_image

def main():
    # Path gambar
    image_path = 'gambar apel.jpeg'
    
    # Membaca gambar
    original_image = cv2.imread(image_path) 

    if original_image is None:
        print("Error: Gambar tidak dapat dibaca.")
        return
    
    dx = int(input("Masukkan pergeseran horizontal (dx): "))
    dy = int(input("Masukkan pergeseran vertikal (dy): "))
    
    # Mendapatkan gambar hasil transformasi
    transformed_image = translate(original_image, dx, dy)

    # Menampilkan gambar asli
    cv2.imshow("Original Image", original_image)

    # Menampilkan gambar hasil transformasi
    cv2.imshow("Transformed Image", transformed_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
