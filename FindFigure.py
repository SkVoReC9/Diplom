import cv2
import imutils
import numpy as np
import FindFunc

#Read source img
img = cv2.imread('IMG\Test.png')
gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gr = cv2.GaussianBlur(gr, (3, 3), 0)
edge = cv2.Canny(gr, 10, 250)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)
cnts = cv2.findContours(closed.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
new_img = FindFunc.FindElement(imgGray, img)
cv2.imshow('res.png', new_img)
cv2.waitKey(0)


