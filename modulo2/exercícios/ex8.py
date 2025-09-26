class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        raise NotImplementedError("Subclasses devem implementar este método")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Cachorro")

    def fazer_som(self):
        return "Au Au"

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Gato")

    def fazer_som(self):
        return "Miau"

cachorro1 = Cachorro("Rex")
gato1 = Gato("Mimi")

print(f"{cachorro1.nome} é um {cachorro1.especie} e faz: {cachorro1.fazer_som()}")
print(f"{gato1.nome} é um {gato1.especie} e faz: {gato1.fazer_som()}")