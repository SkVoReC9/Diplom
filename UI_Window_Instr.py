import sys

from PyQt5 import QtWidgets, QtGui

import InstructionWindow
import UI_Window_Start


class Instr_Window(QtWidgets.QMainWindow):
    def __init__(self, CSS_NAME, JS_NAME, HTMLON):
        super(Instr_Window, self).__init__()
        self.ui = InstructionWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Инструкция')
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        #Переменные настроек
        self.SettCSS = CSS_NAME
        self.SettJS = JS_NAME
        self.SettHTML = HTMLON

        ###BANNER###
        Pic_ban = QtWidgets.QLabel(self)
        pixmap_ban = QtGui.QPixmap('IMG1\\baner.png')
        Pic_ban.setPixmap(pixmap_ban)
        Pic_ban.resize(pixmap_ban.width(), pixmap_ban.height())
        Pic_ban.move(50,25)

        Label_For_Pic = QtWidgets.QLabel(self)
        Label_For_Pic.setText('Это баннер он используется для отображения информации или картинки')
        Label_For_Pic.setStyleSheet('color:white; font:bold;')
        Label_For_Pic.adjustSize()
        Label_For_Pic.move(110, 80)
        ###

        ###MAIN###
        Pic_main = QtWidgets.QLabel(self)
        pixmap_main = QtGui.QPixmap('IMG1\\main.png')
        Pic_main.setPixmap(pixmap_main)
        Pic_main.resize(pixmap_main.width(), pixmap_main.height())
        Pic_main.move(50, 250)

        Label_For_Pic1 = QtWidgets.QLabel(self)
        Label_For_Pic1.setText('Это главный контент сайта, чаще замещается текстом или статьей')
        Label_For_Pic1.setStyleSheet('color:white; font:bold;')
        Label_For_Pic1.adjustSize()
        Label_For_Pic1.move(350, 300)
        ###

        ###IMAGEBLOCK###
        Pic_img = QtWidgets.QLabel(self)
        pixmap_img = QtGui.QPixmap('IMG1\\img.png')
        Pic_img.setPixmap(pixmap_img)
        Pic_img.resize(pixmap_img.width(), pixmap_img.height())
        Pic_img.move(50, 400)

        Label_For_Pic2 = QtWidgets.QLabel(self)
        Label_For_Pic2.setText('Это картинка она используется для отображения как главного контента')
        Label_For_Pic2.setStyleSheet('color:white; font:bold;')
        Label_For_Pic2.adjustSize()
        Label_For_Pic2.move(400, 450)
        ###

        ###SCROLL###
        Pic_scr = QtWidgets.QLabel(self)
        pixmap_scr = QtGui.QPixmap('IMG1\\scr.png')
        Pic_scr.setPixmap(pixmap_scr)
        Pic_scr.resize(pixmap_scr.width(), pixmap_scr.height())
        Pic_scr.move(50, 550)

        Label_For_Pic3 = QtWidgets.QLabel(self)
        Label_For_Pic3.setText('Это карусель элементов, на ней распологаются обычно разделы сайта или товары')
        Label_For_Pic3.setStyleSheet('color:white; font:bold;')
        Label_For_Pic3.adjustSize()
        Label_For_Pic3.move(275, 575)
        ###

        ###LOWER_MENU###
        Pic_low = QtWidgets.QLabel(self)
        pixmap_low = QtGui.QPixmap('IMG1\\low.png')
        Pic_low.setPixmap(pixmap_low)
        Pic_low.resize(pixmap_low.width(), pixmap_low.height())
        Pic_low.move(50, 650)

        Label_For_Pic3 = QtWidgets.QLabel(self)
        Label_For_Pic3.setText('Это нижний блок сайта, используется для навигации')
        Label_For_Pic3.setStyleSheet('color:white; font:bold;')
        Label_For_Pic3.adjustSize()
        Label_For_Pic3.move(275, 675)
        ###

        #Подключение к кнопке функции
        self.ui.StartLoad.clicked.connect(self.BeginLoad)

    #Функция запуска окна работы
    def BeginLoad(self):
        self.open = UI_Window_Start.Start_Window(self.SettCSS, self.SettJS, self.SettHTML)
        self.open.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    InstrWin = Instr_Window()
    InstrWin.show()
    sys.exit(app.exec_())