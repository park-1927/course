import cv2
import numpy as np
from matplotlib import pyplot as plt

#�̹����� ��ȭ���� ���� �����ڸ� ���� ���

#Sobel ���, Scharr ���,Laplacian ����� ����
#���� Sobel�� Scharr�� ��ȭ���� ������ ������ x�� y������ ������ �� ��dma
#Sobel�� ��� Ŀ�� ����� ũ�⸦ ������ �� �ִ� ���ڰ� ������
#Scharr�� ���� ����� ũ�⸦ �����ϴ� ���ڰ� ��dma
#Laplacian�� ��ȭ���� ���� ������ �����ϴ� ����� �ƴϰ�
#��ü ���������� �����ڸ��� �����ϸ� Ŀ�� ����� ũ�⸦ ������ �� ����



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
