class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.__salario = salario
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, novo_salario):
        self.__salario = novo_salario

    def apresentar(self):
        print(f"{super().apresentar()}, Disciplina: {self.disciplina}, Salário: {self.__salario}")

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
    
    def apresentar(self):
        print(f"{super().apresentar()}, Matrícula: {self.matricula}, Curso: {self.curso}")

professor = Professor("Ana", 35, "Matemática", 5000.00)

aluno = Aluno("Carlos", 20, "2023001", "Engenharia")

professor.apresentar()
aluno.apresentar()