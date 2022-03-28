import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from cadastro2 import *

class Cadastro_2(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)



if __name__ == '__main__':
    qt= QApplication(sys.argv)
    cadastro1= Cadastro_1()
    cadastro1.show()
    qt.exec_()




