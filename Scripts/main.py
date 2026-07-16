import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('../Original Images/image.png')

gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.show()

cropped_img=img[150:250, 300:400]
plt.imshow(cropped_img)
plt.show()

height, width=img.shape[:2]
center=(width//2, height//2)
matrix=cv2.getRotationMatrix2D(center, 45, 1)
rotated=cv2.warpAffine(img, matrix, (width, height))
plt.imshow(rotated)
plt.show()

brightness=np.ones(img.shape, dtype=np.uint8) * 50
brighter=cv2.add(img, brightness)
plt.imshow(brighter)
plt.show()

cv2.imwrite("../Output images/gray.png", gray)
cv2.imwrite("../Output images/cropped.png", cropped_img)
cv2.imwrite("../Output images/rotated.png", rotated)
cv2.imwrite("../Output images/brighter.png", brighter)

