import cv2

# 이미지 파일을 읽어온다
img = cv2.imread('cat.jpg')

# 이미지의 크기를 변경한다
resized_img = cv2.resize(img, (100, 100))

# 변경된 이미지를 화면에 표시한다
cv2.imshow('Resized Image', resized_img)

# 키 입력을 대기한다
cv2.waitKey(0)

# 모든 윈도우를 종료한다
cv2.destroyAllWindows()
