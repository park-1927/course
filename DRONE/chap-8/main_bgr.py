import cv2 # OpenCV API
import matplotlib as plt
image = cv2.imread('apple.jpg', cv2.IMREAD_GRAYSCALE) # 이미지 파일 그레이 스케일로 불러오기
#plt.imshow(image, img)
plt.imshow(image, cmap = 'gray') # 이미지 시각화
plt.show()
