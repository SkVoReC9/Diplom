import sys, webbrowser

import os

from PyQt5 import QtWidgets, QtGui, QtCore

import StartWindow

import FindFigure

class Start_Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Start_Window, self).__init__()
        self.ui = StartWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.OpenFileButton.clicked.connect(self.OpenFile)
        self.ui.StartDetect.clicked.connect(self.Start_Detecting)
        self.ui.OpenHTML.clicked.connect(self.Openhtml)

        global Maket_Name
        global Complete

    def OpenFile(self):
        options = QtWidgets.QFileDialog.Options()
        #options |=QtWidgets.QFileDialog.DontUseNativeDialog
        Maket_Name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "", "Image (*.jpeg *.png *.bmp))", options=options)
        if(Maket_Name):
            self.ui.lineEdit.setText(Maket_Name)
        else:
            self.ui.lineEdit.setText('')

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

    def Openhtml(self):
        new = 2
        url = os.path.dirname(os.path.realpath(__file__)) + '\HTMLBlocks\Construct.html'
        webbrowser.open(url, new=new)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Start_Win = Start_Window()
    Start_Win.show()
    sys.exit(app.exec_())