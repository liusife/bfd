class Conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor} realizado com sucesso."
        else:
            return "Valor de depósito inválido."
        
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso."
        else:
            return "Saldo insuficiente ou valor inválido."
        
    def exibir_saldo(self):
        return f"Saldo atual: R${self.saldo}"
    
conta1 = Conta("João", 1000)
conta2 = Conta("Maria", 500)

print(conta1.exibir_saldo())
print(conta2.depositar(200))
print(conta2.exibir_saldo())