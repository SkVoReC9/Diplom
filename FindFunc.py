import cv2
import pathlib
import numpy as np
from PIL import Image
import os
import imutils

def FindElement(imgGray, img):
    # Dict of templates TODO Save coord for elements
    ###
    images = []
    folder = os.path.dirname(os.path.realpath(__file__)) + '\Templates'
    for filename in os.listdir(folder):
     img_dir = os.path.join(folder, filename)
     if img_dir is not None:
        images.append(img_dir)
    ###

    Arr_of_blocks = []
    #cycle for reading each template from dict
    for i in images:
        template = cv2.imread(i, 1)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        template = cv2.Canny(template, 50, 200)
        w, h = template.shape[::-1]
        found = None
        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            resized = imutils.resize(img, width=int(img.shape[1]*scale))
            r = img.shape[1] / float(resized.shape[1])
            if resized.shape[0] < h or resized.shape[1] < w:
                break
            edg = cv2.Canny(resized, 50, 200)
            res = cv2.matchTemplate(edg, template, cv2.TM_CCOEFF_NORMED)
            (_, maxVal, _, maxLoc) = cv2.minMaxLoc(res)
            #clone = np.dstack([edg, edg, edg])
           # cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
            #               (maxLoc[0] + w, maxLoc[1] + h), (0, 0, 255), 2)
            #cv2.imshow("Visualize", clone)
            #cv2.waitKey(0)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)
            (_, maxLoc, r) = found
            (SX, SY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
            (EX, EY) = (int((maxLoc[0]+w)*r), int((maxLoc[1]+h)*r))
        cv2.rectangle(img, (SX, SY), (EX, EY), (255, 0, 255), 1)
        cv2.putText(img, SX.__str__() + ' ' + SY.__str__() + ' ' + EX.__str__() + ' ' + EY.__str__(), (SX, SY), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
        Arr = [SX, SY, EX, EY, i]
        Arr_of_blocks.append(Arr)

    print(Arr_of_blocks)
    return Arr_of_blocks
