import numpy as np
import cv2
from random import randint

black = np.zeros([720,1280, 1], "uint8")			# create 3d array with uint8 type zeros in them
cv2.imshow("Black", black)
						# to close the window and de-allocate any associated memory usage


white = np.ones([720,1280,3], "uint8")			# create 3d array with uint8 type ones in them
white *= (2**8-1)								# multiple each element

cv2.imshow("White", white)

color = white.copy()							#deep copy
color[:,:]= (randint(0,255),randint(0,255),randint(0,255))

cv2.imshow("color", color)

rainbow = white.copy()
for i in range(720):
	for j in range(1280):
		rainbow[i, j]=(randint(0,255),randint(0,255),randint(0,255))


cv2.imshow("rainbow", rainbow)

cv2.imwrite("rainbow.jpg", rainbow)
cv2.imwrite("color.jpg", color)
cv2.imwrite("white.jpg", white)
cv2.imwrite("black.jpg", black)

cv2.waitKey(0)
cv2.destroyAllWindows()	
