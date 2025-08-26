numero1 = int(input("Digite um número inteiro: "))
numero2 = int(input("Digite outro número inteiro: "))
numero3 = int(input("Digite mais um número inteiro: "))

maior_numero = max(numero1, numero2, numero3)
menor_numero = min(numero1, numero2, numero3)
somatorio = sum([numero1, numero2, numero3])

print(f"O maior número é: {maior_numero}")
print(f"O menor número é: {menor_numero}")
print(f"A soma dos três números é: {somatorio}")
