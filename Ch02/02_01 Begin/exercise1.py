import numpy as np
import cv2

img = cv2.imread("opencv-logo.png")   			# import img
cv2.namedWindow("image", cv2.WINDOW_NORMAL)		# to display image cv2.WINDOW_NORMAL can be replaced by 0
cv2.imshow("Image", img)						# to show
#cv2.waitKey(0)									# wait until a key be pressed
#cv2.waitKey(1000)								# wait for 1000ms then close
cv2.imwrite("output.jpg", img)					# save the final image
