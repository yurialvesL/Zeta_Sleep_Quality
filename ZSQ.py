import sys
from Tela_logado import*
from Tela_login import *
from cadastro import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QDialog,QSpinBox,QRadioButton,QMessageBox,QDialog,QListWidget,QComboBox,QTableView
from PyQt5.QtGui import *
from editar import * 
from Tela_logado import *
from getpass import getpass
from mysql.connector import connect, Error
from Data.Usuario import Usuario
from Data.Solucao import Solucao
from Data.ListadeSolucao import ListadeSolucao
from Data.Usuario import *
from Tela_Admin import *
from BD.Connector import *
from cadastro_Adm import *
from editar_Adm import *

import numpy as np
import random
import pandas as pd

edilene = ""

cpfG = ""



class editar_Adm(QMainWindow,Ui_editar_Adm):
      usuario_edt = Usuario(0,"","","",0,0,0,0,0,0,0,0,0,"")
      def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        self.btn_goCadastro2.clicked.connect(self.guarda_dado)
      
      def pega_usuario(self,usuarioAtual):
        
        self.usuario_edt = usuarioAtual
        print(self.usuario_edt.id)
        self.preenche_dado()
      

     
      
      def preenche_dado(self):
          self.txt_nome.setText(self.usuario_edt.nome)
          self.txt_cpf.setText(self.usuario_edt.cpf)
          self.txt_senha.setText(self.usuario_edt.senha)
          self.txt_idade.setText(str(self.usuario_edt.idade))
          self.spinHorasDormidas.setValue(self.usuario_edt.hrsono)
          self.spinExercicioSemana.setValue(self.usuario_edt.exerc)
          self.spinXicarasCafe.setValue(self.usuario_edt.cafe)
          self.spinExercicioSemana_2.setValue(self.usuario_edt.stressnv)
          if self.usuario_edt.sexo ==0:
              self.Sexo_Feminino_2.setChecked(True)
          elif self.usuario_edt.sexo == 1:
              self.Sexo_masculino_2.setChecked(True)
          if self.usuario_edt.sonoagitado==1:
              self.Sono_AgitadoSim_2.setChecked(True)
          elif self.usuario_edt.sonoagitado==0:
              self.Sono_AgitadoNao_2.setChecked(True)          
          if self.usuario_edt.alcooloucigarro==0:
              self.Drogalicita_NAO_2.setChecked(True)
          elif self.usuario_edt.alcooloucigarro==1:
              self.Drogalicita_SIM_2.setChecked(True)
          if self.usuario_edt.admin==0:
              self.Adm_NAO.setChecked(True)
          elif self.usuario_edt.admin==1:
              self.Adm_SIM.setChecked(True)


        
      def guarda_dado(self):
           nome = self.txt_nome.text()
           cpf = self.txt_cpf.text()
           senha = self.txt_senha.text()
           idade = self.txt_idade.text()
           horas = self.spinHorasDormidas.value()
           cafe = self.spinXicarasCafe.value()
           dias = self.spinExercicioSemana.value()
           strees = self.spinExercicioSemana_2.value()

           if self.Sexo_Feminino_2.isChecked():

               sexo = 0
           if self.Sexo_masculino_2.isChecked():
               sexo = 1
           if self.Sono_AgitadoSim_2.isChecked():
               agitado = 1
           if self.Sono_AgitadoNao_2.isChecked():
               agitado = 0
           if self.Drogalicita_NAO_2.isChecked():
               droga = 0
           if self.Drogalicita_SIM_2.isChecked():
               droga = 1
           if self.Adm_NAO.isChecked():
               adm=0
           if self.Adm_SIM.isChecked():
               adm=1
           usuario_edt = Usuario(0,nome,senha,cpf,adm,idade,sexo,horas,cafe,droga,dias,agitado,strees,0)
           cpf_antigo=self.usuario_edt.cpf
           dataset = pd.read_csv('registrosTreinamentoIa.csv')
           X = dataset.iloc[:, :-1].values
           y = dataset.iloc[:, -1].values


            #Dividindo os dados em um grupo de treino e um grupo de teste
           from sklearn.model_selection import train_test_split
           X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

            #print (X_train)

            #print(y_train)

            #print(X_test)

            #print(y_test)

            #Redimensionando os dados pra virarem valores entre -3 e 3 pro módulo de
            #machine learning poder trabalhar
           from sklearn.preprocessing import StandardScaler
           sc = StandardScaler()
           X_train = sc.fit_transform(X_train)
           X_test = sc.transform(X_test)

            #Confirmando o redimensionamento
            #print(X_train)


            #Treinando o modulo Random Forest Classification com o grupo de dados de treino
           from sklearn.ensemble import RandomForestClassifier
           classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
           classifier.fit(X_train, y_train)

            #Fazendo a previsão dos resultados do grupo de teste
            #y_pred = classifier.predict(X_test)
            #print(np.concatenate((y_pred.reshape(len(y_pred),1),
            #y_test.reshape(len(y_test),1)),1))

            #Fazendo a confusion matrix pra saber a acurácia do módulo
            #from sklearn.metrics import confusion_matrix, accuracy_score
            #cm = confusion_matrix(y_test, y_pred)
            #print(cm)
           problema = str(classifier.predict(sc.transform([[usuario_edt.idade, usuario_edt.sexo, usuario_edt.hrsono, usuario_edt.cafe, usuario_edt.alcooloucigarro, usuario_edt.exerc, usuario_edt.sonoagitado, usuario_edt.stressnv]])))
            
           b= problema.split('[')
           bom=str(b[1])
           c= bom.split(']')
           print(c)
           problema_final = c[0].strip(" '' ")
            
           prob_antigo=usuario_edt.prob

           self.usuario_edt.prob = problema_final
           
           cpf_pravalidar1=self.usuario_edt.cpf
           cpf_pravalidar1=cpf_pravalidar1.replace('-','')
           cpf_pravalidar1=cpf_pravalidar1.replace('.','')

           if Connector.valida_cpf(cpf_pravalidar1):
               if Connector.check_cpf(self,self.usuario_edt.cpf):
                   Connector.editUsuario_ADM(self,self.usuario_edt,cpf_antigo)

                   if prob_antigo!=problema_final:
                        if Connector.check_solution(self,self.usuario_edt.id,self.usuario_edt.prob):
                            solucao= Solucao(problema_final,0,self.usuario_edt.id,0,0,0,0) 
                            Connector.insertSolucao(self,solucao)
               
                   usu_atualizado= QMessageBox()
                   usu_atualizado.setWindowIcon(QIcon('icone (1).png'))
                   usu_atualizado.setWindowTitle('Atualização de Usuário')
                   usu_atualizado.setIcon(QMessageBox.Information)
                   usu_atualizado.setText(f'Usuário atualizado com sucesso! ')
                   usu_atualizado.setStandardButtons(QMessageBox.Ok)
                   usu_atualizado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                   usu_atualizado.exec()
                   self.tAdm = Tela_Admin()
                   self.hide()
                   self.tAdm.show()
               else:
                   usu_atualizado= QMessageBox()
                   usu_atualizado.setWindowIcon(QIcon('icone (1).png'))
                   usu_atualizado.setWindowTitle('Erro de atualização de Usuário')
                   usu_atualizado.setIcon(QMessageBox.Warning)
                   usu_atualizado.setText(f'Já existe usuário com este CPF! ')
                   usu_atualizado.setStandardButtons(QMessageBox.Ok)
                   usu_atualizado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                   usu_atualizado.exec()
           else:
               usu_cadastrado= QMessageBox()
               usu_cadastrado.setWindowIcon(QIcon('icone (1).png'))
               usu_cadastrado.setWindowTitle('CPF Inválido!')
               usu_cadastrado.setIcon(QMessageBox.Critical)
               usu_cadastrado.setText(f'Digite um Cpf válido para ser feito o cadastro! ')
               usu_cadastrado.setStandardButtons(QMessageBox.Ok)
               usu_cadastrado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
               usu_cadastrado.exec()


class cadastro_Adm(QMainWindow,Ui_cadastro_Adm):
    nome=''
    cpf=''
    adm=0
    senha=''
    idade=0
    sexo=0
    horaSono=0
    cafe=0
    alcool=0
    exercicio=0
    sonoAgitado=0
    nvlStress=0
    


    


    usuario_adm = Usuario(0,nome,senha,cpf,adm,idade,sexo,horaSono,cafe,alcool,exercicio,sonoAgitado,nvlStress,0)
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_goCadastro2.clicked.connect(self.guarda_adm)
        self.Btn_voltarLogin.clicked.connect(self.voltar)
   
       
    

    

    def guarda_adm(self):
        nome = self.txt_nome.text()
        cpf = self.txt_cpf.text()
        senha = self.txt_senha.text()
        idade = self.txt_idade.text()
        horas = self.spinHorasDormidas.value()
        cafe = self.spinXicarasCafe.value()
        dias = self.spinExercicioSemana.value()
        strees = self.spinExercicioSemana_2.value()

        if self.Sexo_Feminino_2.isChecked():

            sexo = 0
        if self.Sexo_masculino_2.isChecked():
            sexo = 1
        if self.Sono_AgitadoSim_2.isChecked():
            agitado = 1
        if self.Sono_AgitadoNao_2.isChecked():
            agitado = 0
        if self.Drogalicita_NAO_2.isChecked():
            droga = 0
        if self.Drogalicita_SIM_2.isChecked():
            droga = 1
        if self.Adm_NAO.isChecked():
            adm=0
        if self.Adm_SIM.isChecked():
            adm=1

        self.usuario_adm = Usuario(0,nome,senha,cpf,adm,idade,sexo,horas,cafe,droga,dias,agitado,strees,0)

            
        #dataset = pd.read_sql(Connector.collectData(self,usuarioUpdate.prob))            
        dataset = pd.read_csv('registrosTreinamentoIa.csv')
        X = dataset.iloc[:, :-1].values
        y = dataset.iloc[:, -1].values


        #Dividindo os dados em um grupo de treino e um grupo de teste
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

        #print (X_train)

        #print(y_train)

        #print(X_test)

        #print(y_test)

        #Redimensionando os dados pra virarem valores entre -3 e 3 pro módulo de
        #machine learning poder trabalhar
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)

        #Confirmando o redimensionamento
        #print(X_train)


        #Treinando o modulo Random Forest Classification com o grupo de dados de treino
        from sklearn.ensemble import RandomForestClassifier
        classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
        classifier.fit(X_train, y_train)

        #Fazendo a previsão dos resultados do grupo de teste
        #y_pred = classifier.predict(X_test)
        #print(np.concatenate((y_pred.reshape(len(y_pred),1),
        #y_test.reshape(len(y_test),1)),1))

        #Fazendo a confusion matrix pra saber a acurácia do módulo
        #from sklearn.metrics import confusion_matrix, accuracy_score
        #cm = confusion_matrix(y_test, y_pred)
        #print(cm)
        problema = str(classifier.predict(sc.transform([[self.usuario_adm.idade, self.usuario_adm.sexo, self.usuario_adm.hrsono, self.usuario_adm.cafe, self.usuario_adm.alcooloucigarro, self.usuario_adm.exerc, self.usuario_adm.sonoagitado, self.usuario_adm.stressnv]])))
        #problema = problema[::-2]
            
        b= problema.split('[')
        bom=str(b[1])
        c= bom.split(']')
        print(c)
        problema_final = c[0].strip(" '' ")
        self.usuario_adm.prob = problema_final
        cpf_pravalidar1=self.usuario_adm.cpf
        cpf_pravalidar1=cpf_pravalidar1.replace('-','')
        cpf_pravalidar1=cpf_pravalidar1.replace('.','')



        if Connector.valida_cpf(cpf_pravalidar1):
            if Connector.check_cpf(self,self.usuario_adm.cpf):
                Connector.insertUsuario(self,self.usuario_adm)
                self.usuario_adm=Connector.login_usuario(self,self.usuario_adm.cpf)
                sol = Solucao(self.usuario_adm.prob,0,self.usuario_adm.id,0,0,0,0)
                Connector.insertSolucao(self,sol)
        
                usu_atualizado= QMessageBox()
                usu_atualizado.setWindowIcon(QIcon('icone (1).png'))
                usu_atualizado.setWindowTitle('Usuario inserido no banco')
                usu_atualizado.setIcon(QMessageBox.Information)
                usu_atualizado.setText(f'Usuário inserido com sucesso! ')
                usu_atualizado.setStandardButtons(QMessageBox.Ok)
                usu_atualizado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                usu_atualizado.exec()
                self.telaadm = Tela_Admin()
                self.hide()
        
                self.telaadm.show()
                self.telaadm.loadData()
            else:
                    usu_cadastrado= QMessageBox()
                    usu_cadastrado.setWindowIcon(QIcon('icone (1).png'))
                    usu_cadastrado.setWindowTitle('CPF CLONADO!')
                    usu_cadastrado.setIcon(QMessageBox.Critical)
                    usu_cadastrado.setText(f'já existe um usuário cadastrado com esse CPF! ')
                    usu_cadastrado.setStandardButtons(QMessageBox.Ok)
                    usu_cadastrado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                    usu_cadastrado.exec()
        else:
            usu_cadastrado= QMessageBox()
            usu_cadastrado.setWindowIcon(QIcon('icone (1).png'))
            usu_cadastrado.setWindowTitle('CPF Inválido!')
            usu_cadastrado.setIcon(QMessageBox.Critical)
            usu_cadastrado.setText(f'Digite um Cpf válido para ser feito o cadastro! ')
            usu_cadastrado.setStandardButtons(QMessageBox.Ok)
            usu_cadastrado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
            usu_cadastrado.exec()
    def voltar(self):
        self.tela_adm=Tela_Admin()
        self.hide()
        self.tela_adm.show()




    
 
class Tela_Admin(QMainWindow,Ui_Tela_adm):
     people = []
     
     def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.loadData()
        self.Btn_sair.clicked.connect(self.deslogar)
        self.Btn_cadastrousu.clicked.connect(self.cadstro)
        self.Btn_Delete.clicked.connect(self.excluir)
        self.BtnEditar_usuario.clicked.connect(self.editar_adm)
        self.Btn_buscar.clicked.connect(self.filtro)
        
     def filtro(self):
         row=0
         resultados=[]
         print(self.txt_cpf.text())
         for i in self.people:
             if self.txt_cpf.text() == i.cpf:
                 resultados.append(i)
        
         self.tableWidget.setRowCount(len(resultados))
         for i in resultados:
             self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i.nome))
             self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i.senha))
             self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(i.cpf))
             self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.admin)))
             self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(i.idade)))
             self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.sexo)))
             self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(i.hrsono)))
             self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(str(i.cafe)))
             self.tableWidget.setItem(row,8,QtWidgets.QTableWidgetItem(str(i.alcooloucigarro)))
             self.tableWidget.setItem(row,9,QtWidgets.QTableWidgetItem(str(i.exerc)))
             self.tableWidget.setItem(row,10,QtWidgets.QTableWidgetItem(str(i.sonoagitado)))
             self.tableWidget.setItem(row,11,QtWidgets.QTableWidgetItem(str(i.stressnv)))
             self.tableWidget.setItem(row,12,QtWidgets.QTableWidgetItem(i.prob))
             print(i.nome,i.admin,i.idade,i.sexo,i.prob)
             row+=1
         if self.txt_cpf.text()=='..-':
             self.loadData()


             

     def loadData(self):
       
        
         self.people=Connector.collectUsuarios(self)
         row=0
         self.tableWidget.setRowCount(len(self.people))
         for i in self.people:
             self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(i.nome))
             self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(i.senha))
             self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(i.cpf))
             self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(i.admin)))
             self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(i.idade)))
             self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(i.sexo)))
             self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(i.hrsono)))
             self.tableWidget.setItem(row,7,QtWidgets.QTableWidgetItem(str(i.cafe)))
             self.tableWidget.setItem(row,8,QtWidgets.QTableWidgetItem(str(i.alcooloucigarro)))
             self.tableWidget.setItem(row,9,QtWidgets.QTableWidgetItem(str(i.exerc)))
             self.tableWidget.setItem(row,10,QtWidgets.QTableWidgetItem(str(i.sonoagitado)))
             self.tableWidget.setItem(row,11,QtWidgets.QTableWidgetItem(str(i.stressnv)))
             self.tableWidget.setItem(row,12,QtWidgets.QTableWidgetItem(i.prob))
             print(i.nome,i.admin,i.idade,i.sexo,i.prob)
             row+=1
             
    
     def excluir(self):
        rows = sorted(set(index.row() for index in
                      self.tableWidget.selectedIndexes()))
        nome=self.tableWidget.item(rows[0],0).text()
        


        if self.Btn_Delete.clicked:
            m = QMessageBox()
            m.setWindowIcon(QIcon('icone (1).png'))
            m.setWindowTitle('Exclusão de usuário')
            m.setIcon(QMessageBox.Critical)
            m.setText(f'Tem certeza que deseja excluir o usuário "{nome}" ? ')
            m.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
            m.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
            returnvalue = m.exec()
            if returnvalue == QMessageBox.Yes:
                rows = sorted(set(index.row() for index in
                      self.tableWidget.selectedIndexes()))
                cpf=self.tableWidget.item(rows[0],2).text()
                usu_del = Usuario(0,"","","",0,0,0,0,0,0,0,0,0,0)
                for i in self.people:
                    print(i.cpf,cpf)
                    if i.cpf == cpf :
                        usu_del=i
                        print(usu_del)
                        break


                print(usu_del.nome)        
                conet= Connector()
                conet.deleteUsuario(usu_del)
                self.loadData()
                usu_excluido= QMessageBox()
                usu_excluido.setWindowIcon(QIcon('icone (1).png'))
                usu_excluido.setWindowTitle('Exclusão de Usuário')
                usu_excluido.setIcon(QMessageBox.Information)
                usu_excluido.setText(f'Usuário excluido com sucesso! ')
                usu_excluido.setStandardButtons(QMessageBox.Ok)
                usu_excluido.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                usu_excluido.exec()
               
           



        
       
 
     def cadstro(self):
         

          rows = sorted(set(index.row() for index in
                      self.tableWidget.selectedIndexes()))
           
          
          for row in rows:
              print('Row %d is selected' % row)
              
              print(self.tableWidget.item(rows[0],2).text())
          self.adm=cadastro_Adm()
          self.hide()
          self.adm.show()
        
             
              
            
            
            
              
     
     def editar_adm(self):
       rows = sorted(set(index.row() for index in
               self.tableWidget.selectedIndexes()))
       cpf=self.tableWidget.item(rows[0],2).text()
       usu_edit = Usuario(0,"","","",0,0,0,0,0,0,0,0,0,0)
       for i in self.people:
            print(i.cpf,cpf)
            if i.cpf == cpf :
                usu_edit=Connector.login_usuario(self,i.cpf)
                print(usu_edit)
                 
                break
           
       self.edt_adm= editar_Adm()
       self.edt_adm.pega_usuario(usu_edit)
       self.hide()
       self.edt_adm.show()
     def deslogar(self):
       self.deslog = Tela()
       self.hide()
       self.deslog.show()

class Tela_logado(QMainWindow,Ui_Tela_Logado):



        
    edilene = ""
    cpfTela_logado = ""
    usuarioAtual = Usuario(0,"","","",0,0,0,0,0,0,0,0,0,"")
    solucao1=""
    solucao2=""
    solucao3=""
    solucao4=""
    solucaoum="Tenha um horário fixo pra dormir, desligue seus dispositivos 30 minutos antes da hora de dormir e leia um livro antes de dormir"
    solucaodois="pratique exercicios pelo menos 3 vezes na semana pelas manhãs, medite de 10 a 30 minutos por dia e tente beber uma xícara de chá de camomila pouco antes de dormir"
    solucaotres="Pratique exercicios pelo menos 4 vezes por semana as tardes, evite tomar café após as 18:00, tente praticar um pouco de yoga"
    solucaoquatro="Diminua a quantidade de café diária, evite tomar café após as 18:00, diminua a luminosidade dos seus aparelhos eletrônicos a noite"
    
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        
        self.cb_listaSolucao.addItems(["Solução 1","Solução 2","Solução 3","Solução 4"])
        self.cb_listaSolucao.activated[str].connect(self.opcao_selecionada)
        self.lbl_solucaoESCOLHIDA.setText('Tenha um horário fixo pra dormir, desligue seus dispositivos 30 minutos antes da hora de dormir e leia um livro antes de dormir')
        self.Btn_editar.clicked.connect(self.edt)
        self.Btn_deslogar.clicked.connect(self.deslogar)
        self.btn_simSolution.clicked.connect(self.sla1)
        self.btn_naoSolution.clicked.connect(self.sla2)
      
    
    
    def pega_usuario(self,usuarioAtual):
        dataset = pd.read_csv('testesMelhorResultadoIa.csv')




       
        N = 40
        d = 6
        ads_selected = []
        numbers_of_rewards_1 = [0] * d
        numbers_of_rewards_0 = [0] * d
        total_reward = 0
        for n in range(0, N):
            ad = 0
            max_random = 0
            for i in range(2, d):
                random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
                if (random_beta > max_random):
                    max_random = random_beta
                    ad = i
            ads_selected.append(ad)
            reward = dataset.values[n, ad]
            if reward == 1:
                numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
            else:
                numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
            total_reward = total_reward + reward
  
        #plt.hist(ads_selected)
        #plt.title('Resultado da melhor Solução')
        #plt.xlabel('Soluções')
        #plt.ylabel('Vezes que ela funcionou')
        #plt.show()

        #print(ads_selected)

        self.solucao1 = ads_selected.count(2)
        self.solucao2 = ads_selected.count(3)
        self.solucao3 = ads_selected.count(4)
        self.solucao4 = ads_selected.count(5)

        

        #Seleção da melhor solução
        melhorSolucao = max(self.solucao1, self.solucao2, self.solucao3, self.solucao4)

    
        
        grupoSolucoes = ""

        if melhorSolucao == self.solucao1:
            grupoSolucoes = "Tenha um horário fixo pra dormir, desligue seus dispositivos 30 minutos antes da hora de dormir e leia um livro antes de dormir"
           
        elif melhorSolucao == self.solucao2:
            grupoSolucoes = "pratique exercicios pelo menos 3 vezes na semana pelas manhãs, medite de 10 a 30 minutos por dia e tente beber uma xícara de chá de camomila pouco antes de dormir"
            
        elif melhorSolucao == self.solucao3:
            grupoSolucoes = "Pratique exercicios pelo menos 4 vezes por semana as tardes, evite tomar café após as 18:00, tente praticar um pouco de yoga"
            
        else:
            grupoSolucoes = "Diminua a quantidade de café diária, evite tomar café após as 18:00, diminua a luminosidade dos seus aparelhos eletrônicos a noite"
          

        
        

        #print(ads_selected)

        
        
        self.usuarioAtual = usuarioAtual
        self.lbl_nomeUsuario.setText(self.usuarioAtual.nome)
        
        self.TextArea_info.appendPlainText(f"Olá {self.usuarioAtual.nome}, pelos dados que coletamos em seu cadastro, idetificamos que seu problema relacionado ao seu sono é ou futuramente poderá ser:\n{self.usuarioAtual.prob.title()}\n você pode escolher uma solução ao lado, que melhor se adequa a sua rotina, porém, a melhor solução é:{grupoSolucoes}")
        print(self.usuarioAtual.prob)


    
    def opcao_selecionada(self):
        opcao=self.cb_listaSolucao.currentText()
        if opcao == "Solução 1":
        
            self.lbl_solucaoESCOLHIDA.setText(self.solucaoum)
        elif opcao == "Solução 2":
            
            self.lbl_solucaoESCOLHIDA.setText(self.solucaodois)
        elif opcao == "Solução 3":
           
            self.lbl_solucaoESCOLHIDA.setText(self.solucaotres)
        elif opcao == "Solução 4":
            
            self.lbl_solucaoESCOLHIDA.setText(self.solucaoquatro)    
    
    def deslogar(self):
        self.deslog = Tela()
        self.hide()
        self.deslog.show()
    def sla1(self):
        print('sim',self.cb_listaSolucao.currentText())
        sol_=Connector.collectSolucao(self,self.usuarioAtual.prob,self.usuarioAtual.id)
        Connector.editSolucao(self,sol_,self.cb_listaSolucao.currentText(),1)
        

    def sla2(self):
        print('nao',self.cb_listaSolucao.currentText())
        sol_=Connector.collectSolucao(self,self.usuarioAtual.prob,self.usuarioAtual.id)
        Connector.editSolucao(self,sol_,self.cb_listaSolucao.currentText(),0)

    def edt(self):
        edilene = True
        self.edit = Editar()
        self.hide()
       
        self.edit.show()
        self.edit.pega_usuario(self.usuarioAtual)
        self.edit.preenche_dados()
 
    
    

        

class Editar(QMainWindow,Ui_editar,QDialog):
    usuarioAtual = Usuario(0,"","","",0,0,0,0,0,0,0,0,0,"")
  


    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_goCadastro2.clicked.connect(self.guardar)
        
       
      

    def tl1(self):
        self.telalog = Tela_logado()
        self.hide()
        self.telalog.show()

    def pega_usuario(self,usuarioAtual):
       self.usuarioAtual = usuarioAtual
    
    def preenche_dados(self):
          self.txt_idade.setText(str(self.usuarioAtual.idade))
          self.spinHorasDormidas.setValue(self.usuarioAtual.hrsono)
          self.spinExercicioSemana.setValue(self.usuarioAtual.exerc)
          self.spinXicarasCafe.setValue(self.usuarioAtual.cafe)
          self.spinExercicioSemana_2.setValue(self.usuarioAtual.stressnv)
          if self.usuarioAtual.sexo ==0:
              self.Sexo_Feminino.setChecked(True)
          elif self.usuarioAtual.sexo == 1:
              self.Sexo_masculino.setChecked(True)
          if self.usuarioAtual.sonoagitado==1:
              self.Sono_AgitadoSim.setChecked(True)
          elif self.usuarioAtual.sonoagitado==0:
              self.Sono_AgitadoNao.setChecked(True)          
          if self.usuarioAtual.alcooloucigarro==0:
              self.Drogalicita_NAO.setChecked(True)
          elif self.usuarioAtual.alcooloucigarro==1:
              self.Drogalicita_SIM.setChecked(True)
        
    def guardar(self):
            
            idade = self.txt_idade.text()
            horas = self.spinHorasDormidas.value()
            cafe = self.spinXicarasCafe.value()
            dias = self.spinExercicioSemana.value()
            strees = self.spinExercicioSemana_2.value()

            if self.Sexo_Feminino.isChecked():
                 sexo = 0
             
            if self.Sexo_masculino.isChecked():
                sexo = 1
            if self.Sono_AgitadoSim.isChecked():
                 agitado = 1
            if self.Sono_AgitadoNao.isChecked():
                agitado = 0
            if self.Drogalicita_NAO.isChecked():
                droga = 0
            if self.Drogalicita_SIM.isChecked():
                droga = 1
            usuarioUpdate = Usuario(self.usuarioAtual.id,self.usuarioAtual.nome,self.usuarioAtual.senha,self.usuarioAtual.cpf,self.usuarioAtual.admin,idade,sexo,horas,cafe,droga,dias,agitado,strees,self.usuarioAtual.prob)
           
            dataset = pd.read_csv('registrosTreinamentoIa.csv')
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:, -1].values


            #Dividindo os dados em um grupo de treino e um grupo de teste
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

            #print (X_train)

            #print(y_train)

            #print(X_test)

            #print(y_test)

            #Redimensionando os dados pra virarem valores entre -3 e 3 pro módulo de
            #machine learning poder trabalhar
            from sklearn.preprocessing import StandardScaler
            sc = StandardScaler()
            X_train = sc.fit_transform(X_train)
            X_test = sc.transform(X_test)

            #Confirmando o redimensionamento
            #print(X_train)


            #Treinando o modulo Random Forest Classification com o grupo de dados de treino
            from sklearn.ensemble import RandomForestClassifier
            classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
            classifier.fit(X_train, y_train)

            #Fazendo a previsão dos resultados do grupo de teste
            #y_pred = classifier.predict(X_test)
            #print(np.concatenate((y_pred.reshape(len(y_pred),1),
            #y_test.reshape(len(y_test),1)),1))

            #Fazendo a confusion matrix pra saber a acurácia do módulo
            #from sklearn.metrics import confusion_matrix, accuracy_score
            #cm = confusion_matrix(y_test, y_pred)
            #print(cm)
            problema = str(classifier.predict(sc.transform([[usuarioUpdate.idade, usuarioUpdate.sexo, usuarioUpdate.hrsono, usuarioUpdate.cafe, usuarioUpdate.alcooloucigarro, usuarioUpdate.exerc, usuarioUpdate.sonoagitado, usuarioUpdate.stressnv]])))
            
            b= problema.split('[')
            bom=str(b[1])
            c= bom.split(']')
            print(c)
            problema_final = c[0].strip(" '' ")
            
           
            prob_antigo=usuarioUpdate.prob


            usuarioUpdate.prob = problema_final
            Connector.editUsuario(self,usuarioUpdate)
            if prob_antigo!=problema_final:
                if Connector.check_solution(self,usuarioUpdate.id,usuarioUpdate.prob):
                    solucao= Solucao(problema_final,0,usuarioUpdate.id,0,0,0,0) 
                    Connector.insertSolucao(self,solucao)
            usu_atualizado= QMessageBox()
            usu_atualizado.setWindowIcon(QIcon('icone (1).png'))
            usu_atualizado.setWindowTitle('Atualização de Usuário')
            usu_atualizado.setIcon(QMessageBox.Information)
            usu_atualizado.setText(f'Usuário atualizado com sucesso! ')
            usu_atualizado.setStandardButtons(QMessageBox.Ok)
            usu_atualizado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
            usu_atualizado.exec()
            
                        
         

            self.telalog = Tela_logado()
            self.hide()
            self.telalog.pega_usuario(usuarioUpdate)
            self.telalog.show()
    
class Cadastro(QMainWindow,Ui_cadastro1,QDialog):
    nome = ""
    cpf = ""
    adm=0
    senha = ""
    idade = 0
    horas = 0
    cafe = 0
    dias = 0
    strees = 0
    droga = 0
    sexo = 0
    agitado = 0
  
    usuario1 = Usuario(0,nome,senha,cpf,0,idade,sexo,horas,cafe,droga,dias,agitado,strees,0)      

    def __init__(self, parent=None):
        

        super().__init__(parent)
        super().setupUi(self)
        self.btn_goCadastro2.clicked.connect(self.guardar)
        self.Btn_voltar.clicked.connect(self.voltar)
        

    def guardar(self):
            nome = self.txt_nome.text()
            cpf = self.txt_cpf.text()
            senha = self.txt_senha.text()
            idade = self.txt_idade.text()
            horas = self.spinHorasDormidas.value()
            cafe = self.spinXicarasCafe.value()
            dias = self.spinExercicioSemana.value()
            strees = self.spinExercicioSemana_2.value()

            if self.Sexo_Feminino.isChecked():
                 sexo = 0
            if self.Sexo_masculino.isChecked():
                sexo = 1
            if self.Sono_AgitadoSim.isChecked():
                 agitado = 1
            if self.Sono_AgitadoNao.isChecked():
                agitado = 0
            if self.Drogalicita_NAO.isChecked():
                droga = 0
            if self.Drogalicita_SIM.isChecked():
                droga = 1
            self.usuario1 = Usuario(0,nome,senha,cpf,0,idade,sexo,horas,cafe,droga,dias,agitado,strees,0)

            
                
            dataset = pd.read_csv('registrosTreinamentoIa.csv')
            X = dataset.iloc[:, :-1].values
            y = dataset.iloc[:, -1].values


            
            from sklearn.model_selection import train_test_split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


            
            from sklearn.preprocessing import StandardScaler
            sc = StandardScaler()
            X_train = sc.fit_transform(X_train)
            X_test = sc.transform(X_test)



            
            from sklearn.ensemble import RandomForestClassifier
            classifier = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
            classifier.fit(X_train, y_train)

            
            problema = str(classifier.predict(sc.transform([[self.usuario1.idade, self.usuario1.sexo, self.usuario1.hrsono, self.usuario1.cafe, self.usuario1.alcooloucigarro, self.usuario1.exerc, self.usuario1.sonoagitado, self.usuario1.stressnv]])))
            
            
            b= problema.split('[')
            bom=str(b[1])
            c= bom.split(']')
            print(c)
            problema_final = c[0].strip(" '' ")
            
            self.usuario1.prob = problema_final
            cpf_pravalidar1=self.usuario1.cpf
            cpf_pravalidar1=cpf_pravalidar1.replace('-','')
            cpf_pravalidar1=cpf_pravalidar1.replace('.','')
            if Connector.valida_cpf(cpf_pravalidar1):
                if Connector.check_cpf(self,self.usuario1.cpf):
                    print(self.usuario1.prob)
            
                    Connector.insertUsuario(self,self.usuario1)
                    self.usuario1=Connector.login_usuario(self,self.usuario1.cpf)
                    sol = Solucao(self.usuario1.prob,0,self.usuario1.id,0,0,0,0)
                    Connector.insertSolucao(self,sol)
           
                    usu_cadastrado= QMessageBox()
                    usu_cadastrado.setWindowIcon(QIcon('icone (1).png'))
                    usu_cadastrado.setWindowTitle('Boas Vindas')
                    usu_cadastrado.setIcon(QMessageBox.Information)
                    usu_cadastrado.setText(f'Seja bem vindo ao Zeta Sleep Quality ')
                    usu_cadastrado.setStandardButtons(QMessageBox.Ok)
                    usu_cadastrado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                    usu_cadastrado.exec()
            
                    self.telalog = Tela_logado()
                    self.hide()
                    self.telalog.pega_usuario(self.usuario1)
                    self.telalog.show()
                else:
                    usu_cadastrado= QMessageBox()
                    usu_cadastrado.setWindowIcon(QIcon('icone (1).png'))
                    usu_cadastrado.setWindowTitle('CPF CLONADO!')
                    usu_cadastrado.setIcon(QMessageBox.Warning)
                    usu_cadastrado.setText(f'já existe um usuário cadastrado com esse CPF! ')
                    usu_cadastrado.setStandardButtons(QMessageBox.Ok)
                    usu_cadastrado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                    usu_cadastrado.exec()
            else:
                usu_cadastrado= QMessageBox()
                usu_cadastrado.setWindowIcon(QIcon('icone (1).png'))
                usu_cadastrado.setWindowTitle('CPF Inválido!')
                usu_cadastrado.setIcon(QMessageBox.Critical)
                usu_cadastrado.setText(f'Digite um Cpf válido para ser feito o cadastro! ')
                usu_cadastrado.setStandardButtons(QMessageBox.Ok)
                usu_cadastrado.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
                usu_cadastrado.exec()
    
    def voltar(self):
        self.voltar_login=Tela()
        self.hide()
        self.voltar_login.show()

               
 
          

   

        
    

    
           
class Tela(QMainWindow,Ui_ZSQ_login,QDialog):
    conector = Connector()
    
    

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btn_login.clicked.connect(self.logar)
        
  
         

        self.btn_cadastro.clicked.connect(self.cd1)
       

       
    
    def cd1(self):
        self.cadastro1 = Cadastro()
        self.hide()
        self.cadastro1.show()

  
  
 
   
    def logar(self):
        cpf = self.usuarioCPF.text()
        
        senha = self.senhaUsuario.text()
        UsuarioX = Usuario(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
        UsuarioX = Connector.login_usuario(self,cpf)
       
        if senha == UsuarioX.senha:
           
            print("Deu bom")
            if UsuarioX.admin == 1:
                self.telaadm =Tela_Admin()
                self.hide()
                self.telaadm.show()
            else:

                self.telalog = Tela_logado()
                self.hide()
                self.telalog.show()
                print(UsuarioX)
                if self.telalog.isActiveWindow():
               
                   self.telalog.pega_usuario(UsuarioX)

        
        else:
            usu_errouSenha= QMessageBox()
            usu_errouSenha.setWindowIcon(QIcon('icone (1).png'))
            usu_errouSenha.setWindowTitle('Error')
            usu_errouSenha.setIcon(QMessageBox.Information)
            usu_errouSenha.setText(f'Sua senha está incorreta')
            usu_errouSenha.setStandardButtons(QMessageBox.Ok)
            usu_errouSenha.setStyleSheet("QMessageBox { color:white; background-color:#0055aa;} QLabel{color:white;} QPushButton{color:white;background-color: rgb(94, 197, 230); font-weight:bold}")
            usu_errouSenha.exec()
   
    
if __name__ == '__main__':
        qt = QApplication(sys.argv)
        tela = Tela()
        tela.show()
        sys.exit(qt.exec_())
    
    

            

     
    

    




    
    
    
    
