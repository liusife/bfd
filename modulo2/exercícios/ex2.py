class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

retangulo1 = Retangulo(5, 10)
retangulo2 = Retangulo(3, 4)

print(f"Área do retângulo 1: {retangulo1.calcular_area()}")
print(f"Área do retângulo 2: {retangulo2.calcular_area()}")