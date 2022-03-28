import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Tela_logado import *

class TelaLogado(QMainWindow,Ui_Tela_Logado):
      def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)


if __name__ == '__main__':
    qt= QApplication(sys.argv)
    cadastro1= Cadastro_1()
    cadastro1.show()
    qt.exec_()

   


