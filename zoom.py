import cv2
import numpy as np

def zoom_image(image_path, scale_percent):
    img = cv2.imread(image_path)
    original_width, original_height = img.shape[1], img.shape[0]

    new_width = int(original_width * scale_percent / 100)
    new_height = int(original_height * scale_percent / 100)

    new_size = (new_width, new_height)
    zoomed_img = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
    return zoomed_img

def main():
    image_path = 'apel 2.jpeg'
    scale_percent = 180  # Ubah sesuai kebutuhan

    zoomed_image = zoom_image(image_path, scale_percent)

    cv2.imshow('Citra Asli', cv2.imread(image_path))
    cv2.imshow('Citra Zoomed', zoomed_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
