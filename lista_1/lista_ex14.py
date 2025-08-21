#função para verificar se o número é primo

def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero_usuario = int(input("Digite um número: "))
if eh_primo(numero_usuario):
    print(f"{numero_usuario} é primo!")
else:
    print(f"{numero_usuario} não é primo.")