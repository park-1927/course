import cv2
import numpy as np
import cv2

# �̹��� ������ �о�´�
img = cv2.imread('cat.jpg')

cv2.imshow('original', img)
 
# ä�� ���߱�
saturationScale = 0.01

# �̹����� ���� ������ ��ȯ�ϴ� �� ���
# �� �Լ��� ����Ͽ� �̹����� �پ��� ���� �������� ��ȯ
# �⺻ BGR�� �÷���. GRAY COLOR_BGR2GRAY, COLOR_GRAY2BGR COLOR_RGB2GRAY, COLOR_GRAY2RGB
hsvImage = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)

# HSV �̹����� float32 ���·� ��ȯ
hsvImage = np.float32(hsvImage)
 
# ä�η� �и��ϴ� �Լ�  ( �������� ��� ���)
H, S, V = cv2.split(hsvImage)    # �и���
 
# �������Լ�. np.clip �Լ� �̿��ϸ� 0���� ������ 0���� ���߰�,
# 255���� ũ�� 255�� ���߶� �Ҽ� ����
S = np.clip( S * saturationScale , 0,255 ) # ��갪, �ּҰ�, �ִ밪

# ���⼭�� saturation���� ����
# H,S,V ���� ä���� �ٽ� ��ġ�� �Լ�
hsvImage = cv2.merge( [ H,S,V ] )
 
# ������ float���� �۾�������, �ٽ� uint8�� �����ؾ���
hsvImage = np.uint8(hsvImage)
 
# BGR�� �ٽ� �����ؾ� , �츮�� ������ Ȯ�� ����
imgBgr = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
cv2.imshow('dst', imgBgr)
 
cv2.waitKey()
cv2.destroyAllWindows()
 
