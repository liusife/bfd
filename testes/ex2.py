#testando loops
import random

numero_secreto = random.randint(1, 10)

print("Bem vindo ao loop infinito! Para sair basta acertar o número secreto.")

while True:
    palpite = int(input("Digite um número entre 1 e 10: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número secreto e saiu do loop.")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")