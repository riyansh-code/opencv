#Step 1: Import the Libraries and the image
import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('../Original Images/image.png')# We use the ../ at the start to indicate that the image is in the same project folder but in a different folder as app.py

#Step 2: Conert to grayscale
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray)
plt.show()

#Step 3: Crop Image
cropped_img=img[150:250, 300:400]
plt.imshow(cropped_img)
plt.show()

#Step 4: Rotate image
height, width=img.shape[:2]
center=(width//2, height//2)
matrix=cv2.getRotationMatrix2D(center, 45, 1)
rotated=cv2.warpAffine(img, matrix, (width, height))
plt.imshow(rotated)
plt.show()

#Step 5: Increase brightness by a set amount(50)
brightness=np.ones(img.shape, dtype=np.uint8) * 50
brighter=cv2.add(img, brightness)
plt.imshow(brighter)
plt.show()

#Step 6: Save all outputs in a folder called "Output images"
cv2.imwrite("../Output images/gray.png", gray)#The ../ here also means the same thing as it did when we used it to import the image. Same project folder, but different folder
cv2.imwrite("../Output images/cropped.png", cropped_img)
cv2.imwrite("../Output images/rotated.png", rotated)
cv2.imwrite("../Output images/brighter.png", brighter)

