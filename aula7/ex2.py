import matematica

num1 = int(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+ ou -): ")
num2 = int(input("Digite o segundo número: "))

if operacao == '+':
    resultado = matematica.soma(num1, num2)
elif operacao == '-':
    resultado = matematica.subtracao(num1, num2)
else:
    resultado = "Operação inválida"

print(f"{num1} {operacao} {num2} = {resultado}")