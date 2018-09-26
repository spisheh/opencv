import numpy as np
import cv2

img = cv2.imread("opencv-logo.png", 0)				#1 : defult color   0 : black & white
img.shape											#	number of pix and channels
img.dtype											#	type of channels "uint8" 	
img.size											# 	total number of pixels 

