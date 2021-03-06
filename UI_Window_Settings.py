import sys

from PyQt5 import QtWidgets,QtGui, QtCore

import SettingWindow


class Setting_Window(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super(Setting_Window, self).__init__()
        self.ui = SettingWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Настройки')
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        #Получние родительского класса и переменные настроек
        self.parent1 = parent
        self.CSS_NAME = self.JS_NAME = None
        self.HTMLON = None

        #Подключение функций к кнопками
        self.ui.ExitToMain.clicked.connect(self.close)
        self.ui.ApplyButton.clicked.connect(self.ApplySettings)
        self.ui.CSS_Attach.clicked.connect(self.AttachCSS)
        self.ui.JS_Attach.clicked.connect(self.AttachJS)

    #Функция применения настроек
    def ApplySettings(self):
        if self.ui.HTMLOn.isChecked():
            self.HTMLON = True
            self.parent1.INIT_PARAM(self.CSS_NAME, self.JS_NAME, self.HTMLON)
        else:
            self.parent1.INIT_PARAM(self.CSS_NAME, self.JS_NAME)
        self.close()

    #Функция загрузки CSS файлов
    def AttachCSS(self):
        options = QtWidgets.QFileDialog.Options()
        self.CSS_NAME, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "", "CSS файлы(*.css ))",
                                                            options=options)
        if self.CSS_NAME:
            self.ui.label_2.setStyleSheet('color:green')
        else:
            self.CSS_NAME = None
            self.ui.label_2.setStyleSheet('color:red')

    #Функция загрузки JS файлов
    def AttachJS(self):
        options = QtWidgets.QFileDialog.Options()
        self.JS_NAME, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Открыть файл", "", "JS файлы(*.js ))",
                                                            options=options)
        if self.JS_NAME:
            self.ui.label_3.setStyleSheet('color:green')
        else:
            self.JS_NAME = None
            self.ui.label_3.setStyleSheet('color:red')



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    app1 = Setting_Window()
    app1.show()
    sys.exit(app.exec_())