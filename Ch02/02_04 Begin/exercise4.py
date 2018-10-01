import numpy as np
import cv2

color = cv2.imread("butterfly.jpg",1)
cv2.imshow("Image", color)
cv2.moveWindow("Image", 0, 0)						#where on decktop the window box be

h, w, c = color.shape
b, g, r = cv2.split(color)							#split colors to 3 channel arraies 

split_color = np.empty([h,w*3,3], "uint8" )
zero = np.zeros([h,w,1], "uint8" )
#zero[:,:]=(255)
split_color[:,0:w] = cv2.merge([b,zero,zero])
split_color[:,w:2*w] = cv2.merge([zero,g,zero])
split_color[:,2*w:3*w] = cv2.merge([zero,zero,r])

cv2.imshow("split_color", split_color)
cv2.moveWindow("split_color", 0, h)	
cv2.imwrite("split_color.jpg", split_color)


hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
H1, S1, V1 = cv2.split(hsv)							#split HSV to 3 channel arraies
hsv_split = np.concatenate((H1, S1, V1), axis=1)    #ad them side by side
cv2.imshow("split_color", split_color)
cv2.moveWindow("hsv_split", 0, 2*h)	
cv2.imwrite("hsv_split.jpg", hsv_split)


cv2.waitKey(0)