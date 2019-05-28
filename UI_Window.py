from PyQt5 import QtWidgets, uic
import sys
import DesignerWindow

class myWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWin, self).__init__()
        self.ui = DesignerWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.StartConstruct_Button.clicked(self.StartClicked)

    def StartClicked(self):
        return


app = QtWidgets.QApplication([])
application = myWin()
application.show()
sys.exit(app.exec_())