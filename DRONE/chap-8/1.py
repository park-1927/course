#https://f-lab.kr/insight/python-opencv-basics
#OpenCV를 사용하여 이미지를 불러오고 화면에 표시
#1.py

import cv2

#이미지 파일을 읽어옴
img = cv2.imread('cat.jpg')

#이미지를 화면에 표시
cv2.imshow('image', img)

#키 입력을 대기한다
#waitKey() 함수
#키 입력을 기다리는 대기 함수
#인자 값으로 0 : 무한 대기 / ms(밀리세컨) 단위의 시간을 입력하면
#해당 시간만큼 대기 (1000ms = 1초)
#waitKey의 리턴 값은 키보드로 입력한 키와 동일한 아스키코드 값
cv2.waitKey(0)

# 모든 윈도우를 종료
cv2.destroyAllWindows()
