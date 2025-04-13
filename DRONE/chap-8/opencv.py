import cv2

# 이미지 파일을 읽어온다
img = cv2.imread('apple.jpg')

# 이미지를 화면에 표시한다
cv2.imshow('image', img)

# 키 입력을 대기한다
cv2.waitKey(0)

# 모든 윈도우를 종료한다
cv2.destroyAllWindows()