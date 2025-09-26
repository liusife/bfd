class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        return self.preco

produto1 = Produto("Camisa", 100)
produto2 = Produto("Calça", 150)

print(f"Preço do {produto1.nome}: R${produto1.preco}")
print(f"Preço com pagamento à vista da {produto1.nome}: R${produto1.aplicar_desconto(10)}")

print(f"Preço do {produto2.nome}: R${produto2.preco}")
print(f"Preço com pagamento à vista da {produto2.nome}: R${produto2.aplicar_desconto(20)}")