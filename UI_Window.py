import sys

from PyQt5 import QtWidgets, QtGui

import DesignerWindow
import UI_Window_Instr
import UI_Window_Settings


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = DesignerWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon('Icon.ico'))

        #Переменные для передачи настроек из окна настроек
        self.CSS_ATT = None
        self.JS_ATT = None
        self.HTMLON = None

        #Подключение к кнопкам функции
        self.ui.StartConstruct_Button.clicked.connect(self.StartClicked)
        self.ui.Settings_Button.clicked.connect(self.SettingsClicked)
        self.ui.Exit_Button.clicked.connect(sys.exit)

    #Функция перехода на окно инструкции
    def StartClicked(self):
        self.open = UI_Window_Instr.Instr_Window(self.CSS_ATT, self.JS_ATT, self.HTMLON)
        self.open.show()

    #Функция перехода на окно настроек
    def SettingsClicked(self):
        self.openSet = UI_Window_Settings.Setting_Window(self)
        self.openSet.show()

    #Функция для применения настроек пользователя из окна настроек
    def INIT_PARAM(self, CSS, JS, HTML = False):
        self.CSS_ATT = CSS
        self.JS_ATT = JS
        self.HTMLON = HTML

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())