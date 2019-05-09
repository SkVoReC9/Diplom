from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QToolTip
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        Button_for_start = QPushButton('Start', self)
        Button_for_start.move(100, 100)
        self.resize(1600, 900)
        self.setWindowTitle('SCS')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())