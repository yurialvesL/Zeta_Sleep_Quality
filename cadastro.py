# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cadastro1(object):
    def setupUi(self, cadastro1):
        cadastro1.setObjectName("cadastro1")
        cadastro1.resize(800, 600)
        cadastro1.setMinimumSize(QtCore.QSize(800, 600))
        cadastro1.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icone (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        cadastro1.setWindowIcon(icon)
        cadastro1.setStyleSheet("#cadastro1{\n"
"    \n"
"    \n"
"    background-image:url(C:/Users/Yuri/source/repos/ZSQ/ZSQ/imagens/ceu.png)\n"
"    \n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"#frame{\n"
"\n"
"    border-radius:10px;\n"
"    \n"
"    background-color:#0055aa;\n"
"    \n"
"    \n"
"\n"
"    \n"
"\n"
"\n"
"}\n"
"\n"
"#Btn_voltar\n"
"{\n"
"    border-radius:15px;\n"
"    \n"
"    background-color: rgb(94, 197, 230);\n"
"    \n"
"    border-style:solid;\n"
"\n"
"    font-weight:bold;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"\n"
"\n"
"}\n"
"#btn_goCadastro2\n"
"{\n"
"\n"
"    border-radius:15px;\n"
"    \n"
"    background-color: rgb(94, 197, 230);\n"
"    \n"
"    border-style:solid;\n"
"\n"
"    font-weight:bold;\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"#lbl_estilo{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"\n"
"#spinExerrciciosSemana{\n"
"\n"
"border-radius:10px;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        cadastro1.setIconSize(QtCore.QSize(30, 30))
        self.centralwidget = QtWidgets.QWidget(cadastro1)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_goCadastro2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_goCadastro2.setGeometry(QtCore.QRect(360, 500, 81, 41))
        self.btn_goCadastro2.setStyleSheet("")
        self.btn_goCadastro2.setObjectName("btn_goCadastro2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 331, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.lbl_nome_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_2.setGeometry(QtCore.QRect(140, 120, 133, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_2.setFont(font)
        self.lbl_nome_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_2.setObjectName("lbl_nome_2")
        self.txt_cpf = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_cpf.setGeometry(QtCore.QRect(140, 150, 133, 20))
        self.txt_cpf.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"border:solid;\n"
"border-radius:30px;\n"
"color:white;")
        self.txt_cpf.setInputMask("000.000.000-00")
        self.txt_cpf.setObjectName("txt_cpf")
        self.lbl_nome = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome.setGeometry(QtCore.QRect(320, 110, 133, 45))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome.setFont(font)
        self.lbl_nome.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome.setObjectName("lbl_nome")
        self.txt_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_nome.setGeometry(QtCore.QRect(320, 150, 133, 20))
        self.txt_nome.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"border:solid;\n"
"color:white;")
        self.txt_nome.setObjectName("txt_nome")
        self.lbl_idade = QtWidgets.QLabel(self.centralwidget)
        self.lbl_idade.setGeometry(QtCore.QRect(490, 120, 133, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_idade.setFont(font)
        self.lbl_idade.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_idade.setObjectName("lbl_idade")
        self.txt_idade = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_idade.setGeometry(QtCore.QRect(490, 150, 133, 20))
        self.txt_idade.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"border-style:solid;\n"
"border-radius:15px;\n"
"color:white;")
        self.txt_idade.setObjectName("txt_idade")
        self.lbl_nome_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_3.setGeometry(QtCore.QRect(140, 200, 133, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_3.setFont(font)
        self.lbl_nome_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_3.setObjectName("lbl_nome_3")
        self.lbl_nome_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_4.setGeometry(QtCore.QRect(140, 280, 281, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_4.setFont(font)
        self.lbl_nome_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_4.setObjectName("lbl_nome_4")
        self.spinHorasDormidas = QtWidgets.QSpinBox(self.centralwidget)
        self.spinHorasDormidas.setGeometry(QtCore.QRect(540, 280, 141, 22))
        self.spinHorasDormidas.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"color:white;")
        self.spinHorasDormidas.setObjectName("spinHorasDormidas")
        self.lbl_nome_5 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_5.setGeometry(QtCore.QRect(140, 310, 371, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_5.setFont(font)
        self.lbl_nome_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_5.setObjectName("lbl_nome_5")
        self.spinXicarasCafe = QtWidgets.QSpinBox(self.centralwidget)
        self.spinXicarasCafe.setGeometry(QtCore.QRect(540, 310, 141, 22))
        self.spinXicarasCafe.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"color:white;\n"
"")
        self.spinXicarasCafe.setObjectName("spinXicarasCafe")
        self.lbl_nome_6 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_6.setGeometry(QtCore.QRect(140, 340, 371, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_6.setFont(font)
        self.lbl_nome_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_6.setObjectName("lbl_nome_6")
        self.spinExercicioSemana = QtWidgets.QSpinBox(self.centralwidget)
        self.spinExercicioSemana.setGeometry(QtCore.QRect(540, 340, 141, 22))
        self.spinExercicioSemana.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"color:white;")
        self.spinExercicioSemana.setObjectName("spinExercicioSemana")
        self.lbl_nome_7 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_7.setGeometry(QtCore.QRect(140, 370, 371, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_7.setFont(font)
        self.lbl_nome_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_7.setObjectName("lbl_nome_7")
        self.spinExercicioSemana_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinExercicioSemana_2.setGeometry(QtCore.QRect(540, 370, 141, 22))
        self.spinExercicioSemana_2.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"color:white;")
        self.spinExercicioSemana_2.setObjectName("spinExercicioSemana_2")
        self.lbl_nome_8 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_8.setGeometry(QtCore.QRect(140, 420, 371, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_8.setFont(font)
        self.lbl_nome_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_8.setObjectName("lbl_nome_8")
        self.txt_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_senha.setGeometry(QtCore.QRect(140, 450, 133, 20))
        self.txt_senha.setStyleSheet("background-color: rgb(34, 150, 213);\n"
"border:solid;\n"
"border-radius:30px;\n"
"color:white;")
        self.txt_senha.setInputMask("")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setObjectName("txt_senha")
        self.lbl_nome_9 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_9.setGeometry(QtCore.QRect(310, 200, 161, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_9.setFont(font)
        self.lbl_nome_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_9.setObjectName("lbl_nome_9")
        self.lbl_nome_10 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nome_10.setGeometry(QtCore.QRect(490, 200, 191, 19))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_nome_10.setFont(font)
        self.lbl_nome_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_nome_10.setObjectName("lbl_nome_10")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(80, 30, 641, 541))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Btn_voltar = QtWidgets.QPushButton(self.frame)
        self.Btn_voltar.setGeometry(QtCore.QRect(514, 480, 91, 31))
        self.Btn_voltar.setObjectName("Btn_voltar")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 190, 98, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Sexo_masculino = QtWidgets.QRadioButton(self.layoutWidget)
        self.Sexo_masculino.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Sexo_masculino.setFont(font)
        self.Sexo_masculino.setStyleSheet("color: rgb(255, 255, 255);")
        self.Sexo_masculino.setAutoRepeat(False)
        self.Sexo_masculino.setAutoExclusive(True)
        self.Sexo_masculino.setObjectName("Sexo_masculino")
        self.verticalLayout_4.addWidget(self.Sexo_masculino)
        self.Sexo_Feminino = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Sexo_Feminino.setFont(font)
        self.Sexo_Feminino.setStyleSheet("color: rgb(255, 255, 255);")
        self.Sexo_Feminino.setChecked(False)
        self.Sexo_Feminino.setAutoRepeat(False)
        self.Sexo_Feminino.setAutoExclusive(True)
        self.Sexo_Feminino.setObjectName("Sexo_Feminino")
        self.verticalLayout_4.addWidget(self.Sexo_Feminino)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(230, 190, 54, 54))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Sono_AgitadoSim = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Sono_AgitadoSim.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Sono_AgitadoSim.setFont(font)
        self.Sono_AgitadoSim.setStyleSheet("color: rgb(255, 255, 255);")
        self.Sono_AgitadoSim.setAutoRepeat(False)
        self.Sono_AgitadoSim.setAutoExclusive(True)
        self.Sono_AgitadoSim.setObjectName("Sono_AgitadoSim")
        self.verticalLayout.addWidget(self.Sono_AgitadoSim)
        self.Sono_AgitadoNao = QtWidgets.QRadioButton(self.layoutWidget1)
        self.Sono_AgitadoNao.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Sono_AgitadoNao.setFont(font)
        self.Sono_AgitadoNao.setStyleSheet("color: rgb(255, 255, 255);")
        self.Sono_AgitadoNao.setAutoRepeat(False)
        self.Sono_AgitadoNao.setAutoExclusive(True)
        self.Sono_AgitadoNao.setObjectName("Sono_AgitadoNao")
        self.verticalLayout.addWidget(self.Sono_AgitadoNao)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(410, 190, 54, 54))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Drogalicita_SIM = QtWidgets.QRadioButton(self.layoutWidget2)
        self.Drogalicita_SIM.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Drogalicita_SIM.setFont(font)
        self.Drogalicita_SIM.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.Drogalicita_SIM.setAutoRepeat(False)
        self.Drogalicita_SIM.setAutoExclusive(True)
        self.Drogalicita_SIM.setObjectName("Drogalicita_SIM")
        self.verticalLayout_2.addWidget(self.Drogalicita_SIM)
        self.Drogalicita_NAO = QtWidgets.QRadioButton(self.layoutWidget2)
        self.Drogalicita_NAO.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Drogalicita_NAO.setFont(font)
        self.Drogalicita_NAO.setStyleSheet("color: rgb(255, 255, 255);")
        self.Drogalicita_NAO.setAutoRepeat(False)
        self.Drogalicita_NAO.setAutoExclusive(True)
        self.Drogalicita_NAO.setObjectName("Drogalicita_NAO")
        self.verticalLayout_2.addWidget(self.Drogalicita_NAO)
        self.frame.raise_()
        self.btn_goCadastro2.raise_()
        self.label.raise_()
        self.lbl_nome_2.raise_()
        self.txt_cpf.raise_()
        self.lbl_nome.raise_()
        self.txt_nome.raise_()
        self.lbl_idade.raise_()
        self.txt_idade.raise_()
        self.lbl_nome_3.raise_()
        self.lbl_nome_4.raise_()
        self.spinHorasDormidas.raise_()
        self.lbl_nome_5.raise_()
        self.spinXicarasCafe.raise_()
        self.lbl_nome_6.raise_()
        self.spinExercicioSemana.raise_()
        self.lbl_nome_7.raise_()
        self.spinExercicioSemana_2.raise_()
        self.lbl_nome_8.raise_()
        self.txt_senha.raise_()
        self.lbl_nome_9.raise_()
        self.lbl_nome_10.raise_()
        cadastro1.setCentralWidget(self.centralwidget)

        self.retranslateUi(cadastro1)
        QtCore.QMetaObject.connectSlotsByName(cadastro1)

    def retranslateUi(self, cadastro1):
        _translate = QtCore.QCoreApplication.translate
        cadastro1.setWindowTitle(_translate("cadastro1", "ZSQ - Cadastro"))
        self.btn_goCadastro2.setText(_translate("cadastro1", "Avançar"))
        self.label.setText(_translate("cadastro1", "Dados Pessoais"))
        self.lbl_nome_2.setText(_translate("cadastro1", "CPF"))
        self.lbl_nome.setText(_translate("cadastro1", "Nome"))
        self.lbl_idade.setText(_translate("cadastro1", "Idade"))
        self.lbl_nome_3.setText(_translate("cadastro1", "Qual o seu sexo?"))
        self.lbl_nome_4.setText(_translate("cadastro1", "Quantas horas você dorme por dia:"))
        self.lbl_nome_5.setText(_translate("cadastro1", "Quantas xícaras de café você toma por dia?"))
        self.lbl_nome_6.setText(_translate("cadastro1", "Quantidade de dias que se exercita por semana:"))
        self.lbl_nome_7.setText(_translate("cadastro1", "De 0 a 10 quanto stress você passa:"))
        self.lbl_nome_8.setText(_translate("cadastro1", "Senha"))
        self.lbl_nome_9.setText(_translate("cadastro1", "Seu sono é agitado?"))
        self.lbl_nome_10.setText(_translate("cadastro1", "Você usa drogas lícitas?"))
        self.Btn_voltar.setText(_translate("cadastro1", "Voltar"))
        self.Sexo_masculino.setText(_translate("cadastro1", "Masculino"))
        self.Sexo_Feminino.setText(_translate("cadastro1", "Feminino"))
        self.Sono_AgitadoSim.setText(_translate("cadastro1", "Sim"))
        self.Sono_AgitadoNao.setText(_translate("cadastro1", "Não"))
        self.Drogalicita_SIM.setText(_translate("cadastro1", "Sim"))
        self.Drogalicita_NAO.setText(_translate("cadastro1", "Não"))
