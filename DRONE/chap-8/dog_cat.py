from IPython.display import Image, display

path = "./dog_cat_image.jpg" # 사진 파일의 디렉토리
display(Image(filename = path))


import cv2
import cvlib as cv # cvlib 미설치 시 !pip install cvlib으로 설치 진행

img = cv2.imread(path) # 이미지 파일 불러오기
conf = 0.5 # 사물 인식을 진행할 confidence의 역치 값
model_name = "yolov3" # 사물을 인식할 모델 이름

result = cv.detect_common_objects(img, confidence=conf, model=model_name)


output_path = "/cat_dog_detect.jpg" # 결과가 반영된 이미지 파일 저장 디렉토리

result_img = cv.object_detection.draw_bbox(img, *result) # result 결과를 이미지에 반영
cv2.imwrite(output_path, result_img) # 반영된 이미지 파일 저장
display(Image(filename = output_path)) # 이미지 출력
