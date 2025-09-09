class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario 
    
    def ajustar_salario(self, novo_salario):
        self.salario 


    def apresentar_professor(self):
        return f"Professor {self.nome}, Idade: {self.idade}, Disciplina: {self.disciplina}, Salário: R${self.salario}"