try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    print(f"O resultado de 10 dividido por {numero} é {resultado}")
except ValueError:
    print("Erro: Você deve digitar um número inteiro válido.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")