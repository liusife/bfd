#media de nota de aluno

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"A média é {media}. Aluno aprovado!")
elif media >= 2:
    print(f"A média é {media}. Aluno deverá realizar a prova de recuperação!")
else:
    print(f"A média é {media}. Aluno reprovado!")