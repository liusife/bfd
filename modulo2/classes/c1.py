#aprendendo classes, objetos e metodos

class Carro:
    def __init__(self, marca, modelo, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
    
    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo}, cor: {self.cor}, placa: {self.placa}"

meu_carro = Carro("Toyota", "Corolla", "Prata", "ABC-1234")
carro_amigo = Carro("Volkswagen", "Fusca", "Azul", "XYZ-5678")
print(meu_carro.exibir_informacoes())
print(carro_amigo.exibir_informacoes())