from modelo import Cliente, Compra
from controle import SistemaController

def main():
    sistema = SistemaController()

    # Criando clientes
    c1 = Cliente(1, "Elaine Cristina")
    c2 = Cliente(2, "Chico Science")
    sistema.adicionar_cliente(c1)
    sistema.adicionar_cliente(c2)

    # Criando compras
    compra1 = Compra(101, "2025-09-16", "Rosas", 12, 5.0)
    compra2 = Compra(102, "2025-09-17", "Ganja", 8, 7.5)
    sistema.adicionar_compra(compra1)
    sistema.adicionar_compra(compra2)

    # Exibindo resultados
    print("====== Clientes ======")
    for cliente in sistema.listar_clientes():
        print(cliente)
    
    print("\n====== Compras ======")
    for compra in sistema.listar_compras():
        print(compra)
    

if __name__ == "__main__":
    main()