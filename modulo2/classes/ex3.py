class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso
    
    def apresentar_aluno(self):
        return f"Aluno: {self.nome}, Idade: {self.idade}, Matrícula: {self.matricula}, Curso: {self.curso}"

aluno1 = Aluno("Ana", 20, "2023001", "Engenharia")
print(aluno1.apresentar_aluno())
