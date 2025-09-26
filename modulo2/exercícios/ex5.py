class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def exibir_info(self):
        return f"Nome: {self.nome} \nSalário: R${self.salario}"
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor
    
    def exibir_info(self):
        return f"Nome: {self.nome} \nSalário: R${self.salario} \nSetor: {self.setor}"

gerente1 = Gerente("Carlos", 5000, "Vendas")
funcionario1 = Funcionario("Ana", 3000)

print(gerente1.exibir_info())
print(funcionario1.exibir_info())
