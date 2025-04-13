import cv2

# �̹��� ������ �о�´�
img = cv2.imread('cat.jpg')

# ����þ� ���� �����Ѵ�
# �̹����� ����� ���̰� �ε巯�� ȿ���� �ֱ� ���� ���Ǵ� ����
# a function that blurs an image using a Gaussian filter 
# with a kernel of size 5 x 5 and a standard deviation of 0.
# Ŀ�� ������� ���� ����� Ȧ���� ���� 
# ���� : (3,3) (5,5), (7,7)
# Ŀ�� ����� Ŀ�� ���� �帲ȿ�� ����

#blurred_img = cv2.GaussianBlur(img, (5, 5), 0)


blurred_img = cv2.GaussianBlur(img, (11, 11), 0)

# �� ó���� �̹����� ȭ�鿡 ǥ���Ѵ�
cv2.imshow('Blurred Image', blurred_img)

# Ű �Է��� ����Ѵ�
cv2.waitKey(0)

# ��� �����츦 �����Ѵ�
cv2.destroyAllWindows()
