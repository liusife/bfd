nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))
nota3 = float(input("Digite a sua terceira nota:"))

media_aritmetica = (nota1 + nota2 + nota3) / 3

if media_aritmetica < 7:
    print("Você foi para final")
else:
    print("Você foi aprovado")