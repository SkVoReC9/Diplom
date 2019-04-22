import cv2
import imutils
import numpy as np

#Read source img
img = cv2.imread('Test.png')
gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gr = cv2.GaussianBlur(gr, (3, 3), 0)
edge = cv2.Canny(gr, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)
cnts = cv2.findContours(closed.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    # approx contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    if len(approx) == 4:
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 4)
    # если 3 контура, значит это треугольник
    if len(approx) == 3:
        cv2.drawContours(img, [approx], -1, (255, 0, 0), 4)
    # если больше 5 значит это круг
    if len(approx) > 5:
        cv2.drawContours(img, [approx], -1, (0, 0, 255), 5)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#template = cv2.imread('Test1.png', 0)
#w, h = template.shape[::-1]

#Dict of templates
dict_ = {1: 'Test1.png', 2: 'Test2.png', 3: 'Test3.png'}
   #cycle for reading each template from dict
for i in dict_.values():
    template = cv2.imread(i, 0)
    w, h = template.shape[::-1]
    #getting match from picture
    res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
    conf = cv2.minMaxLoc(res)
    print(conf)
    #need write cord and id for each image, if one template match to 2 objects
    #then need add one id for 2 objects
    threshold = 0.8
    loc = np.where(res>=threshold)
    for pt in zip(*loc[ : :-1]):
        cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow('res.png', img)
cv2.waitKey(0)
