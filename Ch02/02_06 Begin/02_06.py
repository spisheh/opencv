import numpy as np
import cv2

#image = cv2.imread("thresh.jpg")

cv2.imshow("image", image)
blur = cv2.GaussianBlur(image, (5,55), 0)  #blur on y axes

kernel = np.ones((5,5), 'uint8' )

dilate = cv2.dilate(image, kernel, iterations=1)
erode = cv2.erode(image, kernel, iterations=1)

cv2.imwrite("blur.jpg", blur)
cv2.imwrite("dilate.jpg", dilate)
cv2.imwrite("erode.jpg", erode)
