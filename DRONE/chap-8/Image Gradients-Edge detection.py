import cv2
import numpy as np
from matplotlib import pyplot as plt

#이미지의 변화도에 따른 가장자리 추출 방법

#Sobel 방법, Scharr 방법,Laplacian 방법이 있음
#먼저 Sobel과 Scharr은 변화도를 추출할 방향을 x와 y축으로 지정할 수 있dma
#Sobel의 경우 커널 행렬의 크기를 지정할 수 있는 인자가 있지만
#Scharr는 필터 행렬의 크기를 지정하는 인자가 없dma
#Laplacian은 변화도의 추출 방향을 지정하는 방식이 아니고
#전체 방향으로의 가장자리를 추출하며 커널 행렬의 크기를 지정할 수 있음



img = cv2.imread('./Sudoku Original Screenshots and Videos.jpg', 0)
laplacian = cv2.Laplacian(img,cv2.CV_8U,ksize=5)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
