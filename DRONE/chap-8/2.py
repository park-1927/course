import cv2

# �̹��� ������ �о�´�
img = cv2.imread('cat.jpg')

# �̹����� ũ�⸦ �����Ѵ�
resized_img = cv2.resize(img, (100, 100))

# ����� �̹����� ȭ�鿡 ǥ���Ѵ�
cv2.imshow('Resized Image', resized_img)

# Ű �Է��� ����Ѵ�
cv2.waitKey(0)

# ��� �����츦 �����Ѵ�
cv2.destroyAllWindows()
