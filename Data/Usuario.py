class Usuario:

    id = 0
    nome = ""
    senha = ""
    cpf = ""
    admin = 0
    idade = 0
    sexo = 0
    hrsono = 0
    cafe = 0
    alcooloucigarro = 0
    exerc = 0
    sonoagitado = 0
    stressnv = 0
    prob = ""


    def __init__(self, id, nome, senha, cpf, admin, idade, sexo, hrsono, cafe, alcooloucigarro, exerc, sonoagitado, stressnv, prob):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.admin = admin
        self.idade = idade
        self.sexo = sexo
        self.hrsono = hrsono
        self.cafe = cafe
        self.alcooloucigarro = alcooloucigarro
        self.exerc = exerc
        self.sonoagitado = sonoagitado
        self.stressnv = stressnv
        self.prob = prob
