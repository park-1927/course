import cv2
import numpy as np
import cv2

# 이미지 파일을 읽어온다
img = cv2.imread('cat.jpg')

cv2.imshow('original', img)
 
# 채도 낮추기
saturationScale = 0.01

# 이미지의 색상 공간을 변환하는 데 사용
# 이 함수를 사용하여 이미지를 다양한 색상 공간으로 변환
# 기본 BGR의 컬러를. GRAY COLOR_BGR2GRAY, COLOR_GRAY2BGR COLOR_RGB2GRAY, COLOR_GRAY2RGB
hsvImage = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

# HSV 이미지를 float32 형태로 변환
hsvImage = np.float32(hsvImage)
 
# 채널로 분리하는 함수  ( 다차원일 경우 사용)
H, S, V = cv2.split(hsvImage)    # 분리됨
 
# 유용한함수. np.clip 함수 이용하면 0보다 작으면 0으로 맞추고,
# 255보다 크면 255로 맞추라 할수 있음
S = np.clip( S * saturationScale , 0,255 ) # 계산값, 최소값, 최대값

# 여기서는 saturation값만 조정
# H,S,V 나눈 채널을 다시 합치는 함수
hsvImage = cv2.merge( [ H,S,V ] )
 
# 위에서 float으로 작업했으로, 다시 uint8로 변경해야함
hsvImage = np.uint8(hsvImage)
 
# BGR로 다시 변경해야 , 우리가 눈으로 확인 가능
imgBgr = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
cv2.imshow('dst', imgBgr)
 
cv2.waitKey()
cv2.destroyAllWindows()
 
