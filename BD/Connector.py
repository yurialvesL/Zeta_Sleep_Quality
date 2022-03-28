from getpass import getpass
from mysql.connector import connect, Error

from Data.Usuario import Usuario
from Data.Solucao import Solucao
from Data.ListadeSolucao import ListadeSolucao

class Connector:

    #Métodos para Usuarios
    def valida_cpf(cpf):
        

        valida=False
        lista_firstDigit=[10,9,8,7,6,5,4,3,2]
        cpf_inserido=list(cpf)
        cpf_teste=cpf_inserido.copy()
        cpf_teste.pop(-1)
        cpf_teste.pop(-1)
        cpf_testeConvertido=[]
        for l in cpf_teste:
            cpf_testeConvertido.append(int(l))

        lista_firstD =[]
        a=0
        b=0
        for i in cpf_testeConvertido:
            int(i)

            a=i*lista_firstDigit[b]
            lista_firstD.append(a)
            b+=1

        resultado=0
        for l in lista_firstD:
            resultado+=l

        primeiro_digito=(11-(resultado%11))
        if primeiro_digito >9:
            cpf_testeConvertido.append(0)
        else:
            cpf_testeConvertido.append(primeiro_digito)
        print(cpf_testeConvertido)
        list_SecondDigit=[11,10,9,8,7,6,5,4,3,2]
        m=0
        n=0
        list_secondD=[]
        for j in cpf_testeConvertido:
            m=j*list_SecondDigit[n]
            list_secondD.append(m)
            n+=1
        print(f'lista todas as multiplicações {list_secondD}')
        second_result=0
        for p in list_secondD:
            second_result+=p
   
        segundo_digito=(11-(second_result%11))
        print(segundo_digito)
        if segundo_digito >9:
            cpf_testeConvertido.append(0)
        else:
            cpf_testeConvertido.append(segundo_digito)
        print(f'cpf apos inserir o segundo digito:\n {cpf_testeConvertido}')
        cpf_inserido_convertido=[]
        for i in cpf_inserido:
            cpf_inserido_convertido.append(int(i))

        print(f'cpf inserido no começo {cpf_inserido}')

        if (set(cpf_testeConvertido) == set(cpf_inserido_convertido)):
            print('Deu bom')
            valida =True
            return valida
        
        else: 
            print('CPF invalido')
            valida =False
            return valida
        

    def check_cpf(self,cpf):
        try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:

                select_query = "SELECT * FROM zetasleepq.usuarios WHERE CPF = %s;"
                value = (cpf,)
                
               
                with connection.cursor() as cursor:
                    cursor.execute(select_query, value)
                    result = cursor.fetchall()
                    
                    for row in result:
                        print('Já existe pelo amor de deus')
                        return False

                    print('N existe')
                    return True


                        

                
        except Error as e:
                print(e)
                return e
        

    def collectUsuarios(self): #Serve para coletar todos os dados da tabela usuarios do bd
                           #Retorna uma List de objetos Usuario
        try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:

                select_query = "SELECT * FROM zetasleepq.usuarios;"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    lista = []
                    for row in result:
                        Usu = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10], row[11], row[12], row[13])
                        lista.append(Usu)

            return lista

        except Error as e:
            print(e)
            return e
    def login_usuario(self,cpf):
         try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:

                select_query = "SELECT * FROM zetasleepq.usuarios WHERE CPF = %s;"
                value = (cpf,)
                
               
                with connection.cursor() as cursor:
                    cursor.execute(select_query, value)
                    result = cursor.fetchall()
                    Usu=Usuario(0,"","","",0,0,0,0,0,0,0,0,0,"")
                    for row in result:
                        print(row)
                        Usu = Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                      row[10], row[11], row[12], row[13])
                        

                return Usu
         except Error as e:
                print(e)
                return e



    def editUsuario_ADM(self, usu,cpf_antigo): #Recebe a lista em uso e o objeto usuario novo,
                                      # altera os dados no bd e na lista
        print(usu.nome,usu.admin,usu.idade,usu.sexo,usu.prob)
        try:

            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:
                if connection.is_connected():
                    print('deu bom')
                else:
                    print('fodeu')
                cursor = connection.cursor()
               
                sql = "UPDATE zetasleepq.usuarios SET Nome = %s, Senha = %s, CPF = %s, Admin = %s, Idade = %s, Sexo = %s, HorasdeSono = %s, Cafe = %s, AlcoolOuCigarro = %s, Exercícios = %s, SonoAgitado = %s, NvlStress = %s, Previsão = %s WHERE (CPF=%s);"


                values = (usu.nome,usu.senha,usu.cpf,usu.admin,usu.idade,usu.sexo, usu.hrsono, usu.cafe,
                          usu.alcooloucigarro, usu.exerc, usu.sonoagitado, usu.stressnv,usu.prob,cpf_antigo)
                cursor.execute(sql,values)
                connection.commit()
                cursor.close()

                

        except Error as e:
            print(e)
            return None

    def editUsuario(self, usu): #Recebe a lista em uso e o objeto usuario novo,
                                      # altera os dados no bd e na lista
        
        try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:
                cursor = connection.cursor()
                sql = "UPDATE zetasleepq.usuarios SET Idade = %s,Sexo = %s, HorasdeSono = %s, Cafe =%s, AlcoolOuCigarro = %s, Exercícios = %s, SonoAgitado = %s, NvlStress = %s, Previsão = %s WHERE (CPF = %s);"


                values = (usu.idade,usu.sexo, usu.hrsono, usu.cafe,
                          usu.alcooloucigarro, usu.exerc, usu.sonoagitado, usu.stressnv,usu.prob, usu.cpf)
                cursor.execute(sql,values)
                connection.commit()
                cursor.close()

                

        except Error as e:
            print(e)
            return None

    def insertUsuario(self, usu): #Usuário pode ter qualquer ID,
                                        # ao ser registrado no banco, ele recebe o
                                        # id do auto_increment e é atualizado

        try:
            with connect(
                    host="localhost",
                    user="root",  # Alterar dados para o seu mysql
                    password="admin",
                    database="zetasleepq",
            ) as connection:
                cursor = connection.cursor()
                sql = "INSERT INTO `zetasleepq`.`usuarios` (`Nome`, `Senha`, `CPF`, `Admin`, `Idade`, `Sexo`,"\
                " `HorasdeSono`, `Cafe`, `AlcoolOuCigarro`, `Exercícios`, `SonoAgitado`, `NvlStress`, `Previsão`) " \
                      "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

                values = (usu.nome, usu.senha, usu.cpf, usu.admin, usu.idade, usu.sexo, usu.hrsono, usu.cafe,
                          usu.alcooloucigarro, usu.exerc, usu.sonoagitado, usu.stressnv, usu.prob)
                cursor.execute(sql, values)
                connection.commit()
               
                
                cursor.close()
                

                
                

        except Error as e:
            print(e)
            return None%s

    def deleteUsuario(self,usuario): #recebe a lista em uso e o id do usuario para deletar
        
        self.deleteSolucoes(usuario.id)
        

        try:
            with connect(
                    host="localhost",
                    user="root",  # Alterar dados para o seu mysql
                    password="admin",
                    database="zetasleepq",
            ) as connection:
                cursor = connection.cursor()
                sql = "DELETE FROM `zetasleepq`.`usuarios` WHERE (`CPF` = %s)"
                id = (usuario.cpf,)
                cursor.execute(sql, id)
                connection.commit()

               

        except Error as e:
            print(e)
            return None

    #Métodos para Soluções
    def collectSolucao(self,tipo,idUsu):
          try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:
                
                 if tipo == "ansiedade":
                    sql="SELECT * FROM zetasleepq.sol_ansiedade where idUsu = %s "
                 elif tipo == "insonia":
                    sql="SELECT * FROM zetasleepq.sol_insonia where idUsu = %s "
                 elif tipo == "paralisia do sono":
                     sql="SELECT * FROM zetasleepq.sol_paralisiadosono where idUsu = %s "
                 elif tipo == "pesadelos":
                    sql="SELECT * FROM zetasleepq.sol_pesadelos where idUsu = %s "
                 elif tipo == "pernas inquietas":
                    sql="SELECT * FROM zetasleepq.sol_sindromepernasinquietas where idUsu = %s "
                    
                 elif tipo == "sonambulismo":
                     sql="SELECT * FROM zetasleepq.sol_sonambulismo where idUsu = %s "
                 elif tipo == "sonolencia diurna":
                     sql="SELECT * FROM zetasleepq.sol_sonolenciadiurna where idUsu = %s "
                      


                 with connection.cursor() as cursor:
                    values=(idUsu,)
                    cursor.execute(sql,values)
                    result = cursor.fetchall()
                    
                    for row in result:
                        sol = Solucao(tipo,row[0], row[1], row[2], row[3], row[4], row[5])
                        
                       
                   
                    return sol

          except Error as e:
                print(e)
                return None


    def collectSolucoes(self,numSol): #numSol = Número do tipo de solução
        # 0 = ansiedade, 1 = bruxismo, 2 = insonia, 3 = paralisiads
        # 4 = pesadelos, 5 = sinperninquieta, 6 = sonambulismo, 7 = Sonodiurna

        try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:

                if numSol == 0 :
                    select_query = "SELECT * FROM `sol_ansiedade`"
                elif numSol == 1:
                    select_query = "SELECT * FROM `sol_bruxismo`"
                elif numSol == 2:
                    select_query = "SELECT * FROM `sol_insonia`"
                elif numSol == 3:
                    select_query = "SELECT * FROM `sol_paralisiadosono`"
                elif numSol == 4:
                    select_query = "SELECT * FROM `sol_pesadelos`"
                elif numSol == 5:
                    select_query = "SELECT * FROM `sol_sindromepernasinqueitas`"
                elif numSol == 6:
                    select_query = "SELECT * FROM `sol_sonambulismo`"
                elif numSol == 7:
                    select_query = "SELECT * FROM `sol_sonolenciadiurna`"
                else:
                    raise Exception("Tipo de Solução não encontrado")  # Joga erro se não houver este tipo de solução

                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    lista = []
                    for row in result:
                        Sol = Solucao(row[0], row[1], row[2], row[3], row[4], row[5])
                        lista.append(Sol)
                    lisSol = ListadeSolucao(numSol, lista)
                    return lisSol

        except Error as e:
            print(e)
            return None

    def editSolucao(self,sol,numSol,efetivo): #Recebe a lista em uso e o objeto usuario novo,
                                      # altera os dados no bd e na lista
        na=Solucao("",0,0,0,0,0,0)
        try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:
                cursor = connection.cursor()
                if sol.tipo == "ansiedade":
                    sql="UPDATE `zetasleepq`.`sol_ansiedade` SET `solucao1` = %s, `solucao2` = %s, `solucao3` = %s, `solucao4` = %s WHERE (`idUsu` = %s);"
                elif sol.tipo == "insonia":
                    sql="UPDATE `zetasleepq`.`sol_insonia` SET `solucao1` = %s, `solucao2` = %s, `solucao3` = %s, `solucao4` = %s WHERE (`idUsu` = %s);"
                elif sol.tipo == "paralisia do sono":
                     sql="UPDATE `zetasleepq`.`sol_paralisiadosono` SET `solucao1` = %s, `solucao2` = %s, `solucao3` = %s, `solucao4` = %s WHERE (`idUsu` = %s);"
                elif sol.tipo == "pesadelos":
                    sql="UPDATE `zetasleepq`.`sol_pesadelos` SET `solucao1` = %s, `solucao2` = %s, `solucao3` = %s, `solucao4` = %s WHERE (`idUsu` = %s);"
                elif sol.tipo == "pernas inquietas":
                     sql="UPDATE `zetasleepq`.`sol_sindromepernasinquietas` SET `solucao1` = %s, `solucao2` = %s, `solucao3` = %s, `solucao4` = %s WHERE (`idUsu` = %s);"
                elif sol.tipo == "sonambulismo":
                     sql="UPDATE `zetasleepq`.`sol_sonambulismo` SET `solucao1` = %s, `solucao2` = %s, `solucao3` = %s, `solucao4` = %s WHERE (`idUsu` = %s);"
                elif sol.tipo == "sonolencia diurna":
                     sql="UPDATE `zetasleepq`.`sol_sonolenciadiurna` SET `solucao1` = %s, `solucao2` = %s, `solucao3` = %s, `solucao4` = %s WHERE (`idUsu` = %s);"
                
                if numSol == 'Solução 1':
                    values=(efetivo,sol.solucao2,sol.solucao3,sol.solucao4,sol.idusu)
                elif numSol == 'Solução 2':
                    values=(sol.solucao1,efetivo,sol.solucao3,sol.solucao4,sol.idusu)
                elif numSol == 'Solução 3':
                    values=(sol.solucao1,sol.solucao2,efetivo,sol.solucao4,sol.idusu)
                elif numSol == 'Solução 4':
                    values=(sol.solucao1,sol.solucao2,sol.solucao3,efetivo,sol.idusu)     
                  
                
                cursor.execute(sql,values)
                connection.commit()
                cursor.close()
                                
        except Error as e:
            print(e)
            return None

    def insertSolucaoLista(self, sol_list, ins_sol): #Usuário pode ter qualquer ID,
                                        # ao ser registrado no banco, ele recebe o
                                        # id do auto_increment e é atualizado

        if sol_list.tipo == 0:
            sol_table = "`sol_ansiedade`"
        elif sol_list.tipo == 1:
            sol_table = "`sol_bruxismo`"
        elif sol_list.tipo == 2:
            sol_table = "`sol_insonia`"
        elif sol_list.tipo == 3:
            sol_table = "`sol_paralisiadosono`"
        elif sol_list.tipo == 4:
            sol_table = "`sol_pesadelos`"
        elif sol_list.tipo == 5:
            sol_table = "`sol_sindromepernasinqueitas`"
        elif sol_list.tipo == 6:
            sol_table = "`sol_sonambulismo`"
        elif sol_list.tipo == 7:
            sol_table = "`sol_sonolenciadiurna`"

        try:
            with connect(
                    host="localhost",
                    user="root",  # Alterar dados para o seu mysql
                    password="admin",
                    database="zetasleepq",
            ) as connection:
                cursor = connection.cursor()
                sql = "INSERT INTO `zetasleepq`.%s (`DormirCedo`, `ExerciciosLev`, `ExerciciosMed`," \
                      " `MenosCafe`, `Terapia`) VALUES (%s, %s, %s, %s, %s)"

                values = (sol_table, new_sol.dormirCedo, new_sol.exerciciosLev, new_sol.exerciciosMed, new_sol.menosCafe, new_sol.terapia)
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                ins_sol.id = cursor.lastrowid
                sol_list.lista.append(ins_sol)

        except Error as e:
            print(e)
            return 
    def insertSolucao(self,  solucao): #Usuário pode ter qualquer ID,
                                    # ao ser registrado no banco, ele recebe o
                                    # id do auto_increment e é atualizado

        print('entrei no insert')
        try:
            with connect(
                    host="localhost",
                    user="root",  # Alterar dados para o seu mysql
                    password="admin",
                    database="zetasleepq",
            ) as connection:
                cursor = connection.cursor()
                if solucao.tipo == "ansiedade":
                    sql="INSERT INTO zetasleepq.sol_ansiedade (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                elif solucao.tipo == "insonia":
                    sql="INSERT INTO zetasleepq.sol_insonia (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                    print('passei de insert')
                elif solucao.tipo == "paralisia do sono":
                    sql="INSERT INTO zetasleepq.sol_paralisiadosono (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                elif solucao.tipo == "pesadelos":
                    sql="INSERT INTO zetasleepq.sol_pesadelos (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                elif solucao.tipo == "pernas inquietas":
                    sql="INSERT INTO zetasleepq.sol_sindromepernasinquietas (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                elif solucao.tipo == "sonambulismo":
                    sql="INSERT INTO zetasleepq.sol_sonambulismo (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                elif solucao.tipo == "sonolencia diurna":
                    sql="INSERT INTO zetasleepq.sol_sonolenciadiurna (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                else:
                    print('Fudeu')
                
                #sql = "INSERT INTO `zetasleepq`.%s (`idUsu`, `solucao1`, `solucao2`, `solucao3`, `solucao4`) VALUES (%s, %s, %s, %s, %s);"
                

                values = (solucao.idusu,  solucao.solucao1,  solucao.solucao2,solucao.solucao3,  solucao.solucao4)
                print(solucao.idusu)
                cursor.execute(sql, values)
                connection.commit()
                cursor.close()
                

        except Error as e:
            print(e)
            return None

    def deleteSolucoes(self, id_usu):  

        try:
            with connect(
                    host="localhost",
                    user="root",  # Alterar dados para o seu mysql
                    password="admin",
                    database="zetasleepq",
            ) as connection:
                    cursor = connection.cursor()
                    sql="DELETE FROM `zetasleepq`.`sol_ansiedade` WHERE (`idUsu` = %s);"
                    id = (id_usu,)
                    cursor.execute(sql, id)
                    connection.commit()
                    sql="DELETE FROM `zetasleepq`.`sol_insonia` WHERE (`idUsu` = %s);"
                    id = (id_usu,)
                    cursor.execute(sql, id)
                    connection.commit()
                    sql="DELETE FROM `zetasleepq`.`sol_paralisiadosono` WHERE (`idUsu` = %s);"
                    id = (id_usu,)
                    cursor.execute(sql, id)
                    connection.commit()
                    sql="DELETE FROM `zetasleepq`.`sol_pesadelos` WHERE (`idUsu` = %s);"
                    id = (id_usu,)
                    cursor.execute(sql, id)
                    connection.commit()
                    sql="DELETE FROM `zetasleepq`.`sol_sindromepernasinquietas` WHERE (`idUsu` = %s);"
                    id = (id_usu,)
                    cursor.execute(sql, id)
                    connection.commit()
                    sql="DELETE FROM `zetasleepq`.`sol_sonambulismo` WHERE (`idUsu` = %s);"
                    id = (id_usu,)
                    cursor.execute(sql, id)
                    connection.commit()
                    sql="DELETE FROM `zetasleepq`.`sol_sonolenciadiurna` WHERE (`idUsu` = %s);"
                    id = (id_usu,)
                    cursor.execute(sql, id)
                    connection.commit()
                
                
            
                
            cursor.close()

        except Error as e:
            print(e)
            return None

    def deleteSolucao(self, id_usu,tipo):
        
       
      
        

        try:
            with connect(
                    host="localhost",
                    user="root",  # Alterar dados para o seu mysql
                    password="admin",
                    database="zetasleepq",
            ) as connection:
                if tipo == "ansiedade":
                    sql="DELETE FROM `zetasleepq`.`sol_ansiedade` WHERE (`idUsu` = %s);"
                elif tipo == "insonia":
                    sql="DELETE FROM `zetasleepq`.`sol_insonia` WHERE (`idUsu` = %s);"        
                elif tipo == "paralisia do sono":
                    sql="DELETE FROM `zetasleepq`.`sol_paralisiadosono` WHERE (`idUsu` = %s);"
                elif tipo == "pesadelos":
                    sql="DELETE FROM `zetasleepq`.`sol_pesadelos` WHERE (`idUsu` = %s);"
                elif tipo == "pernas inquietas":
                    sql="DELETE FROM `zetasleepq`.`sol_sindromepernasinquietas` WHERE (`idUsu` = %s);"
                elif tipo == "sonambulismo":
                    sql="DELETE FROM `zetasleepq`.`sol_sonambulismo` WHERE (`idUsu` = %s);"
                elif tipo == "sonolencia diurna":
                    sql="DELETE FROM `zetasleepq`.`sol_sonolenciadiurna` WHERE (`idUsu` = %s);"
                cursor = connection.cursor()
                
                id = (id_usu,)
                cursor.execute(sql, id)
                connection.commit()
               
                
                cursor.close()

        except Error as e:
            print(e)
            return None
    

    def check_solution(self,id_usu,tipo):
         try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:
                
                 if tipo == "ansiedade":
                    sql="SELECT idUsu FROM zetasleepq.sol_ansiedade WHERE idUsu= %s"
                 elif tipo == "insonia":
                    sql="SELECT idUsu FROM zetasleepq.sol_insonia WHERE idUsu= %s "
                 elif tipo == "paralisia do sono":
                     sql="SELECT idUsu FROM zetasleepq.sol_paralisiadosono WHERE idUsu= %s"
                 elif tipo == "pesadelos":
                    sql="SELECT idUsu FROM zetasleepq.sol_pesadelos WHERE idUsu= %s "
                 elif tipo == "pernas inquietas":
                    sql="SELECT idUsu FROM zetasleepq.sol_sindromepernasinquietas WHERE idUsu= %s "
                 elif tipo == "sonambulismo":
                     sql="SELECT idUsu FROM zetasleepq.sol_sonambulismo WHERE idUsu= %s"
                 elif tipo == "sonolencia diurna":
                     sql="SELECT idUsu FROM zetasleepq.sol_sonolenciadiurna WHERE idUsu= %s"
                      


                 with connection.cursor() as cursor:
                    values=(id_usu,)
                    cursor.execute(sql,values)
                    result = cursor.fetchall()
                    cursor.close()
                    for row in result:
                        print('Já existe pelo amor de deus')
                        return False

                    print('N existe')
                    return True
                    
                        
                       
                   
                    

         except Error as e:
                print(e)
                return None


    def collectData(self,tipo):
          try:
            with connect(
                host="localhost",
                user="root",              #Alterar dados para o seu mysql
                password="admin",
                database="zetasleepq",
            ) as connection:
                
                 if tipo == "ansiedade":
                    sql="SELECT solucao1,solucao2,solucao3,solucao4 FROM zetasleepq.sol_ansiedade "
                 elif tipo == "insonia":
                    sql="SELECT solucao1,solucao2,solucao3,solucao4 FROM zetasleepq.sol_insonia "
                 elif tipo == "paralisia do sono":
                     sql="SELECT solucao1,solucao2,solucao3,solucao4 FROM zetasleepq.sol_paralisiadosono "
                 elif tipo == "pesadelos":
                    sql="SELECT solucao1,solucao2,solucao3,solucao4 FROM zetasleepq.sol_pesadelos "
                 elif tipo == "pernas inquietas":
                    sql="SELECT solucao1,solucao2,solucao3,solucao4 FROM zetasleepq.sol_sindromepernasinquietas "
                    
                 elif tipo == "sonambulismo":
                     sql="SELECT solucao1,solucao2,solucao3,solucao4 FROM zetasleepq.sol_sonambulismo "
                 elif tipo == "sonolencia diurna":
                     sql="SELECT solucao1,solucao2,solucao3,solucao4 FROM zetasleepq.sol_sonolenciadiurna "
                      


                 with connection.cursor() as cursor:
                    
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    
                    
                        
                       
                   
                    return result

          except Error as e:
                print(e)
                return None