#https://f-lab.kr/insight/python-opencv-basics
#OpenCV�� ����Ͽ� �̹����� �ҷ����� ȭ�鿡 ǥ��
#1.py

import cv2

#�̹��� ������ �о��
img = cv2.imread('cat.jpg')

#�̹����� ȭ�鿡 ǥ��
cv2.imshow('image', img)

#Ű �Է��� ����Ѵ�
#waitKey() �Լ�
#Ű �Է��� ��ٸ��� ��� �Լ�
#���� ������ 0 : ���� ��� / ms(�и�����) ������ �ð��� �Է��ϸ�
#�ش� �ð���ŭ ��� (1000ms = 1��)
#waitKey�� ���� ���� Ű����� �Է��� Ű�� ������ �ƽ�Ű�ڵ� ��
cv2.waitKey(0)

# ��� �����츦 ����
cv2.destroyAllWindows()
