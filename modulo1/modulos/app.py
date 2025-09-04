import matematica

numero1 = int(input("Digite um número inteiro: "))
escolha = input("Escolha a operação (+, -, *, /): ")
numero2 = int(input("Digite outro número inteiro: "))

if escolha == '+':
    print(matematica.somar(numero1, numero2))
elif escolha == '-':
    print(matematica.subtrair(numero1, numero2))
elif escolha == '*':
    print(matematica.multiplicar(numero1, numero2))
elif escolha == '/':
    print(matematica.dividir(numero1, numero2))
else:
    print("Operação inválida.")
