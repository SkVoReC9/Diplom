import numpy as np
import FindFunc, HTMLModels, imutils, cv2

#Read source img
img = cv2.imread('SRC\TestMain.png')
gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gr = cv2.GaussianBlur(gr, (3, 3), 0)
edge = cv2.Canny(gr, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)
cnts = cv2.findContours(closed.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
     # approx contour
     peri = cv2.arcLength(c, True)
     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
     if len(approx) == 4:
       cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
     #если 3 контура, значит это треугольник
     elif len(approx) == 3:
       cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
     #если больше 5 значит это сложная фигруа
     elif len(approx) > 5:
        cv2.drawContours(img, [approx], -1, (0, 255, 0), 3)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
List_of_blocks = FindFunc.FindElement(imgGray, img)
HTMLModels.StartConstruct(List_of_blocks)
cv2.imshow('res.png',img)
cv2.waitKey(0)


