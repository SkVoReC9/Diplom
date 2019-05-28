import cv2
import numpy as np
import imutils
import os

src_img = cv2.imread('IMG\TestImageBlock.png', 1)
img_gray = cv2.cvtColor(src_img, cv2.COLOR_BGR2GRAY)
images = []
folder = os.path.dirname(os.path.realpath(__file__))+'\IMG1'
for filename in os.listdir(folder):
    img_dir = os.path.join(folder, filename)
    if img_dir is not None:
        images.append(img_dir)
for image in images:
    template1 = cv2.imread(image, 0)
    w, h = template1.shape[::-1]
    res = cv2.matchTemplate(img_gray, template1, cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(src_img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imshow('res.png', src_img)
cv2.waitKey(0)