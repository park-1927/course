import cv2
import numpy as np

# �̹��� �о �׷��̽����� ��ȯ, ���̳ʸ� ������ ��ȯ
img = cv2.imread("./img/human.jpg")
origin = img.copy()

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127,255,cv2.THRESH_BINARY_INV)

# ��Ʃ�� ã��
contours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL, \
                                        cv2.CHAIN_APPROX_SIMPLE)[-2:]
contr = contours[0]

# ���δ� �簢�� ǥ��(������)
x,y,w,h = cv2.boundingRect(contr)
cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 3)

# �ּ����� �簢�� ǥ��(�ʷϻ�)
rect = cv2.minAreaRect(contr)
box = cv2.boxPoints(rect)   # �߽����� ������ 4���� ������ ��ǥ�� ��ȯ
box = np.int0(box)          # ������ ��ȯ
cv2.drawContours(img, [box], -1, (0,255,0), 3)

# �ּ����� �� ǥ��(�Ķ���)
(x,y), radius = cv2.minEnclosingCircle(contr)
cv2.circle(img, (int(x), int(y)), int(radius), (255,0,0), 2)

# �ּ����� �ﰢ�� ǥ��(��ȫ��)
ret, tri = cv2.minEnclosingTriangle(contr)
cv2.polylines(img, [np.int32(tri)], True, (255,0,255), 2)

# �ּ����� Ÿ�� ǥ��(�����)
ellipse = cv2.fitEllipse(contr)
cv2.ellipse(img, ellipse, (0,255,255), 3)

# �߽��� ����ϴ� ���� ǥ��(������)
[vx,vy,x,y] = cv2.fitLine(contr, cv2.DIST_L2,0,0.01,0.01)
cols,rows = img.shape[:2]
cv2.line(img,(0, int(0-x*(vy/vx) + y)), (cols-1, int((cols-x)*(vy/vx) + y)),(0,0,255),2)

# ��� ���

plt.figure(figsize = (10,6))
imgs = {'origin':origin, 'Bound Fit shapes':img}
for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(1,2,i+1)
    plt.title(k)
    plt.imshow(v[:,:,(2,1,0)])
    plt.xticks([]),plt.yticks([])

plt.show()
