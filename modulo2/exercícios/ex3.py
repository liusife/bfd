class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nAno: {self.ano}\n"
    
    def ligar(self):
        return "O carro está ligado."

carro1 = Carro("Toyota", "Corolla", 2020)
carro2 = Carro("Honda", "Civic", 2019)

print(carro1.exibir_info(), carro1.ligar())
print(carro2.exibir_info())
