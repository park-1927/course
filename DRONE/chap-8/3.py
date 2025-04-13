import cv2

# 이미지 파일을 읽어온다
img = cv2.imread('cat.jpg')

# 가우시안 블러를 적용한다
# 이미지의 노이즈를 줄이고 부드러운 효과를 주기 위해 사용되는 필터
# a function that blurs an image using a Gaussian filter 
# with a kernel of size 5 x 5 and a standard deviation of 0.
# 커널 사이즈는 보통 양수의 홀수로 지정 
# 예시 : (3,3) (5,5), (7,7)
# 커널 사이즈가 커질 수록 흐림효과 증가

#blurred_img = cv2.GaussianBlur(img, (5, 5), 0)


blurred_img = cv2.GaussianBlur(img, (11, 11), 0)

# 블러 처리된 이미지를 화면에 표시한다
cv2.imshow('Blurred Image', blurred_img)

# 키 입력을 대기한다
cv2.waitKey(0)

# 모든 윈도우를 종료한다
cv2.destroyAllWindows()
