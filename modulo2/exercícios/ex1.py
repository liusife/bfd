class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_pessoa(self):
        return f"Nome: {self.nome} \nIdade: {self.idade}"

pessoa1 = Pessoa("Gabriel", 10)
pessoa2 = Pessoa("Ana", 20)

print(pessoa1.exibir_pessoa())
print(pessoa2.exibir_pessoa())