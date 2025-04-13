import cv2
import numpy as np

# 이미지 파일을 읽어온다
img = cv2.imread('cat_1.jpg')

# BGR 색상 공간에서 HSV 색상 공간으로 변환한다
# 이미지의 색상을 숫자로 표현하는 방식을 색공간이라고 하며
# RGB, HSV, YCbCr 등이 대표적인 색공간
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



# 파란색 범위를 정의한다
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])


# 이미지에서 파란색 객체만 추출한다
mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

# 마스크를 원본 이미지에 적용한다
# 마스크(mask)는 이미지의 일부를 가리거나 숨기는 기능을 의미
# 포토샵, 피그마, 유니티 등에서 사용할 수 있음
# 밝은 영역(흰색) 어두운 영역(검은색)으로 나누어져 효과가 나타남
# 즉 흰색 영역은 이미지가 보이게 되고 검은색 영역은 가려지게 됨
result_img = cv2.bitwise_and(img, img, mask=mask)

# 결과 이미지를 화면에 표시한다
cv2.imshow('Blue Objects', result_img)

# 키 입력을 대기한다
cv2.waitKey(0)

# 모든 윈도우를 종료한다
cv2.destroyAllWindows()
