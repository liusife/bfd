import constantes as const

print("Bem vind ao programa de cálculo de área de círculos!")

raio = float(input("Digite o raio do círculo: "))
area = (const.PI * (raio ** 2))
print(f"A área do círculo com raio {raio} é aproximadamente {area:.2f}")