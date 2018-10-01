import numpy as np
import cv2

img = cv2.imread("players.jpg",1)

# Scale image

img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_str = cv2.resize(img, (600,600))
img_str_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)


#cv2.imshow("img_half",img_half)
#cv2.imshow("img_str",img_str)
#cv2.imshow("img_str_near",img_str_near)


# Rotate

M = cv2.getRotationMatrix2D((0,0), -30, 1)						#center, degree, resize
rotated30 = cv2.warpAffine(img, M, (img.shape[1],img.shape[0]))


h, w, c = img.shape
M2 = cv2.getRotationMatrix2D((w/2,h/2), -90, 1)
rotated90 = cv2.warpAffine(img, M2, (img.shape[1],img.shape[0]))
#cv2.imshow("rotated30",rotated30)
#cv2.imshow("rotated90",rotated2)

cv2.imwrite("img_half.jpg",img_half)
cv2.imwrite("img_str.jpg",img_str)
cv2.imwrite("img_str_near.jpg",img_str_near)
cv2.imwrite("rotated30.jpg",rotated30)
cv2.imwrite("rotated90.jpg",rotated90)
cv2.waitKey(0)

