#jogo de adivinhação
import random

numero_aleatorio = random.randint(1,20)

for i in range(5):
    palpite = int(input("Adivinhe um número entre 1 e 20: "))
    
    if palpite < numero_aleatorio:
        print("Seu palpite é muito baixo.")
    elif palpite > numero_aleatorio:
        print("Seu palpite é muito alto.")
    elif palpite == numero_aleatorio:
        print(f"Parabéns! Você acertou o número {numero_aleatorio} em {i+1} tentativas.")
        break
    else:
        print(f"Game Over. O número era {numero_aleatorio}.")
