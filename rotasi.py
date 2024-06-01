import cv2
import numpy as np

def rotate_image(image_path, angle):
    image = cv2.imread(image_path)

    # Mendapatkan tinggi dan lebar citra
    height, width = image.shape[:2]

    # Menghitung titik tengah citra
    center = (width // 2, height // 2)

    # Membuat matriks rotasi
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Melakukan rotasi citra
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    return rotated_image

image_path = 'Disney Princess, lily Z.jpg'
rotation_angle = 45

rotated_image = rotate_image(image_path, rotation_angle)

cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
