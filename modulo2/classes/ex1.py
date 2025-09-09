class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa("Osvaldo", 29)
pessoa2 = Pessoa("Maria", 22)

print(pessoa1.nome, pessoa1.idade)
print(pessoa2.nome, pessoa2.idade)
