##https://f-lab.kr/insight/python-opencv-basics
#image_binary.py
import numpy as np
import cv2
img = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)
k = cv2.waitKey()
if k == ord('s'):
    cv2.imwrite('d:/z.jpg', img)
cv2.destroyAllWindows()
