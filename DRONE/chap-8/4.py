import cv2
import numpy as np

# �̹��� ������ �о�´�
img = cv2.imread('cat_1.jpg')

# BGR ���� �������� HSV ���� �������� ��ȯ�Ѵ�
# �̹����� ������ ���ڷ� ǥ���ϴ� ����� �������̶�� �ϸ�
# RGB, HSV, YCbCr ���� ��ǥ���� ������
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)



# �Ķ��� ������ �����Ѵ�
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])


# �̹������� �Ķ��� ��ü�� �����Ѵ�
mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

# ����ũ�� ���� �̹����� �����Ѵ�
# ����ũ(mask)�� �̹����� �Ϻθ� �����ų� ����� ����� �ǹ�
# ���伥, �Ǳ׸�, ����Ƽ ��� ����� �� ����
# ���� ����(���) ��ο� ����(������)���� �������� ȿ���� ��Ÿ��
# �� ��� ������ �̹����� ���̰� �ǰ� ������ ������ �������� ��
result_img = cv2.bitwise_and(img, img, mask=mask)

# ��� �̹����� ȭ�鿡 ǥ���Ѵ�
cv2.imshow('Blue Objects', result_img)

# Ű �Է��� ����Ѵ�
cv2.waitKey(0)

# ��� �����츦 �����Ѵ�
cv2.destroyAllWindows()
