import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from cadstro import *


class Cadastro_1(QMainWindow,Ui_cadastro1):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        





if __name__ == '__main__':
    qt= QApplication(sys.argv)
    style = """
            Ui_cadastro1{
                background: #fff
            
            }        
    
    
    
    """
    app.setStyleSheet(style)
    cadastro1= Cadastro_1()
    cadastro1.show()
    qt.exec_()



    


