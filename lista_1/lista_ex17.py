#verificar se a palavra é um palíndromo

def eh_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

texto_usuario = input("Digite uma palavra ou frase: ")
if eh_palindromo(texto_usuario):
    print(f"{texto_usuario} é um palíndromo!")
else:
    print(f"{texto_usuario} não é um palíndromo.")