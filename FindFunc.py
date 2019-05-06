import cv2
import numpy as np
import imutils


def FindElement(imgGray, img):
    # Dict of templates TODO Save coord for elements
    dict_ = {1: 'IMG\Test1.png', 2: 'IMG\Test33.png', 3: 'IMG\Test3.png', 4: 'IMG\Test331.png'}
    #cycle for reading each template from dict
    for i in dict_.values():
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
            # clone = np.dstack([edg, edg, edg])
            # cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
            #               (maxLoc[0] + w, maxLoc[1] + h), (0, 0, 255), 2)
            # cv2.imshow("Visualize", clone)
            # cv2.waitKey(0)
            if found is None or maxVal > found[0]:
                found = (maxVal, maxLoc, r)
            (_, maxLoc, r) = found
            (SX, SY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
            (EX, EY) = (int((maxLoc[0]+w)*r), int((maxLoc[1]+h)*r))
            cv2.rectangle(img, (SX, SY), (EX, EY), (255, 0, 255), 1)
        cv2.putText(img, SX.__str__() + ' ' + SY.__str__() + ' ' + EX.__str__() + ' ' + EY.__str__(), (SX, SY), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
        Arr = (SX, SY, EX, EY, i)
        print(Arr)

    return img
#
##
    # Iif = None
    # Iif1 = None
    # dict_ = {1: 'IMG\Test1.png', 2: 'IMG\Test33.png', 3: 'IMG\Test3.png', 4: 'IMG\Test331.png'}
  #  cycle for reading each template from dict
    # for i in dict_.values():
    #     template = cv2.imread(i, 0)
    #     w, h = template.shape[::-1]
       # getting match from picture
        # res = cv2.matchTemplate(imgGray, template, cv2.TM_CCOEFF_NORMED)
        # conf = cv2.minMaxLoc(res)
        # print(conf)
      #  TODO need write cord and id for each image, if one template match to 2 objects then need add one id for 2 objects

        # threshold = 0.8
        # loc = np.where(res >= threshold)
        # for pt in zip(*loc[::-1]):
        #     Iif1 = [pt.__str__(), (pt[0] + w).__str__(), (pt[1] + h).__str__()]
        #     cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        # if(Iif!=Iif1):
        #     cv2.putText(img, pt.__str__()+' ' + (pt[0]+w).__str__()+' '+(pt[1]+h).__str__(), pt, cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), lineType=cv2.LINE_AA)
        # cv2.imshow('Iter{0}'.format(i), img)
        # print(pt.__str__() + ' ' + (pt[0] + w).__str__() + ' ' + (pt[1] + h).__str__())
        # Iif = [pt.__str__ (), (pt[0] + w).__str__(),  (pt[1] + h).__str__()]
###