import sys

from PyQt5 import QtWidgets

import DesignerWindow
import UI_Window_Instr


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = DesignerWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.StartConstruct_Button.clicked.connect(self.StartClicked)
        self.ui.Exit_Button.clicked.connect(sys.exit)

    def StartClicked(self):
        self.open = UI_Window_Instr.Instr_Window()
        self.open.show()


app = QtWidgets.QApplication([])
application = MainWindow()
application.show()
sys.exit(app.exec_())