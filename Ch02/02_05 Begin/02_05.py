import numpy as np
import cv2

im = cv2.imread("butterfly.jpg", 1)
gray = cv2. cvtColor(im, cv2.COLOR_RGB2GRAY)
cv2.imwrite("gray.jpg", gray)

b = im[:,:,0]
g = im[:,:,1]
r = im[:,:,2]
a = ( b[:,:]+g[:,:]+r[:,:] )//3
print(a)
rgba = cv2.merge((b,g,r,a))
cv2.imwrite("rgba.png", rgba)