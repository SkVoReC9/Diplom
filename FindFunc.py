import cv2
import numpy as np
import imutils

def FindElement(imgGray, img):
    # Dict of templates
    dict_ = {1: 'IMG\Test1.png', 2: 'IMG\Test2.png', 3: 'IMG\Test3.png'}
    # cycle for reading each template from dict
    for i in dict_.values():
        template = cv2.imread(i, 0)
        w, h = template.shape[::-1]
        # getting match from picture
        res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
        conf = cv2.minMaxLoc(res)
        print(conf)
        # TODO need write cord and id for each image, if one template match to 2 objects then need add one id for 2 objects
        threshold = 0.74
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    return img
