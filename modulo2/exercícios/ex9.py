class Professor:
    def __init__(self, nome, idade, disciplina):
        self.nome = nome
        self.idade = idade
        self.disciplina = disciplina

    def apresentar(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e ensino {self.disciplina}."

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.disciplina = None

    def matricular(self, disciplina):
        self.disciplina = disciplina
        print(f"{self.nome} foi matriculado na disciplina {self.disciplina}.")

# Exemplo de uso:
prof = Professor("Carlos", 40, "Matemática")
aluno = Aluno("Ana", 18)
print(prof.apresentar())
print(f"Aluna: {aluno.nome}, Idade: {aluno.idade}")
aluno.matricular(prof.disciplina)