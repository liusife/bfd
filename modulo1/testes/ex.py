nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

def calcular_media(n1, n2):
    return (n1 + n2) / 2

media = calcular_media(nota1, nota2)

print(f"A média de {nome} é: {media:.2f}")

