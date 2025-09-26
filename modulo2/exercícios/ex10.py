class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def exibir_carrinho(self):
        print("Produtos no carrinho:")
        for produto in self.produtos:
            print(f"- {produto.nome} (R${produto.preco})")

    def calcular_total(self):
        total = sum(produto.preco for produto in self.produtos)
        print(f"Total: R${total}")

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.carrinho = Carrinho()

    def adicionar_ao_carrinho(self, produto):
        self.carrinho.adicionar_produto(produto)
        print(f"{self.nome} adicionou {produto.nome} ao carrinho.")

# Exemplo de uso:
cliente1 = Cliente("João")
produto1 = Produto("Livro", 30)
produto2 = Produto("Caneta", 5)

cliente1.adicionar_ao_carrinho(produto1)
cliente1.adicionar_ao_carrinho(produto2)
cliente1.carrinho.exibir_carrinho()
cliente1.carrinho.calcular_total()
