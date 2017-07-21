import cv2
import numpy as np

img = cv2.imread('./data/cup.jpg',cv2.IMREAD_COLOR)

#ROI - Region of an Image

img[100:150, 100:150] = [255,255,255]

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()