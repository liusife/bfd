class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome
    
    def __str__(self):
        return f"Cliente[ID: {self.id_cliente}, Nome: {self.nome}]"


class Compra:
    def __init__(self, id_compra, data_compra, produto, quantidade, preco):
        self.id_compra = id_compra
        self.data_compra = data_compra
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
    
    def valor_total(self):
        return self.quantidade * self.preco
    
    def __str__(self):
        return (f"Compra {self.id_compra}: {self.produto}"
                f"({self.quantidade} x R${self.preco:.2f}) em {self.data_compra}"
                f" - Total: R${self.valor_total():.2f}")
    