from IPython.display import Image, display

path = "./dog_cat_image.jpg" # ���� ������ ���丮
display(Image(filename = path))


import cv2
import cvlib as cv # cvlib �̼�ġ �� !pip install cvlib���� ��ġ ����

img = cv2.imread(path) # �̹��� ���� �ҷ�����
conf = 0.5 # �繰 �ν��� ������ confidence�� ��ġ ��
model_name = "yolov3" # �繰�� �ν��� �� �̸�

result = cv.detect_common_objects(img, confidence=conf, model=model_name)


output_path = "/cat_dog_detect.jpg" # ����� �ݿ��� �̹��� ���� ���� ���丮

result_img = cv.object_detection.draw_bbox(img, *result) # result ����� �̹����� �ݿ�
cv2.imwrite(output_path, result_img) # �ݿ��� �̹��� ���� ����
display(Image(filename = output_path)) # �̹��� ���
