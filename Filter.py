import cv2 
from matplotlib import pyplot as plt

image = cv2.imread('bunga.jpg')

blur = cv2.blur(image,(3,3))
width = image.shape[1]
height = image.shape[0]
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# 3x3 mask
blurred_image3 = cv2.blur(image, (3, 3))
cv2.imwrite('blurred_image3.png', blurred_image3)

# 5x5 mask
blurred_image5 = cv2.blur(image, (10, 10))
cv2.imwrite('blurred_image5.png', blurred_image5)

plt.subplot(121),plt.imshow(image),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blurred_image5),plt.title('Blurred')
plt.show()
