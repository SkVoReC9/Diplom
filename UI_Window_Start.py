import os
import sys
import time
import webbrowser

from PyQt5 import QtWidgets, QtGui

import FindFigure
import StartWindow


class Start_Window(QtWidgets.QMainWindow):
    def __init__(self, SettCSS, SettJS, SettHTML):
        super(Start_Window, self).__init__()
        self.ui = StartWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Обработка')
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        #Переменные настроек
        self.CSS = SettCSS
        self.JS = SettJS
        self.HTML = SettHTML

        #Подключение кнопок к функциям
        self.ui.OpenFileButton.clicked.connect(self.OpenFile)
        self.ui.StartDetect.clicked.connect(self.Start_Detecting)
        self.ui.OpenHTML.clicked.connect(self.Openhtml)

        #Установка значения только для чтения
        self.ui.lineEdit.setReadOnly(True)

        #Установка глобальной видимости
        global Maket_Name
        global Complete

    #Функция открытия файла
    def OpenFile(self):
        options = QtWidgets.QFileDialog.Options()
        #options |=QtWidgets.QFileDialog.DontUseNativeDialog
        Maket_Name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "", "Image (*.jpeg *.png *.bmp))", options=options)
        if(Maket_Name):
            self.ui.lineEdit.setText(Maket_Name)
        else:
            self.ui.lineEdit.setText('')

    #Функция считывания шаблона
    def Start_Detecting(self):
        i = 0
        if self.ui.lineEdit.text() == '':
            self.ui.label_2.setText('Ошибка!Выберите изображение')
            self.ui.label_2.setStyleSheet('color:red')
            self.ui.label_2.adjustSize()
            return
        else:
            Maket = self.ui.lineEdit.text()
            Complete = FindFigure.Start_Detect(Maket)
            Comp = open(Complete, 'r')
            for line in Comp.readlines():
                self.ui.progressBar.setValue(i)
                self.ui.label_2.setText('Обработка')
                self.ui.label_2.setStyleSheet('color:green')
                self.ui.label_2.adjustSize()
                i = i + 1
            Comp.close()
            self.ui.label_2.setText('Успешно!')
            self.ui.label_2.setStyleSheet('color:green')
            self.ui.label_2.adjustSize()
            self.ui.StartDetect.setEnabled(False)
            self.ui.OpenHTML.setEnabled(True)
    #Функция открытия браузера и HTML файла с ним, если указан параметр то открывает и блокнот
    def Openhtml(self):
        new = 2
        url = os.path.dirname(os.path.realpath(__file__)) + '\HTMLBlocks\Construct.html'
        webbrowser.open(url, new=new)
        if self.HTML:
            import subprocess as sp
            Name = 'notepad.exe'
            fileName = os.path.dirname(os.path.realpath(__file__)) + '\HTMLBlocks\Construct.html'
            sp.Popen([Name, fileName])
        time.sleep(15)
        fileName1 = open(os.path.dirname(os.path.realpath(__file__)) + '\HTMLBlocks\Construct.html', 'w')
        fileName2 = open(os.path.dirname(os.path.realpath(__file__)) + '\HTMLBlocks\Construct1.html', 'r')
        fileName1.write(fileName2)
        fileName2.close()
        fileName1.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Start_Win = Start_Window()
    Start_Win.show()
    sys.exit(app.exec_())