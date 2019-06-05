import FindFunc
import HTMLModels
import cv2
import imutils

def Start_Detect(FileName):
#Считывание полученного изображения и преобразования его для обработки
    img = cv2.imread(FileName)
    gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gr = cv2.GaussianBlur(gr, (3, 3), 0)
    edge = cv2.Canny(gr, 10, 250)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edge, cv2.MORPH_CLOSE, kernel)
    cnts = cv2.findContours(closed.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
     # Сглаживание контуров
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
    #Получаем список блоков
    List_of_blocks = FindFunc.FindElement(imgGray, img)
    #Получаем готовый файл
    File_Ready = HTMLModels.StartConstruct(List_of_blocks)
    return File_Ready


