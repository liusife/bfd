import random

numero_secreto = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    
    if palpite < numero_secreto:
        print("Seu palpite é muito baixo.")
    elif palpite > numero_secreto:
        print("Seu palpite é muito alto.")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto}.")
        break