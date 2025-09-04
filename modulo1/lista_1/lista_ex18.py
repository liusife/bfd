#Substituir palavras em uma frase

frase = input("Digite uma frase: ")
palavra_antiga = input("Digite a palavra a ser substituída: ")
palavra_nova = input("Digite a nova palavra: ")

if palavra_antiga not in frase:
    print(f"A palavra '{palavra_antiga}' não foi encontrada na frase.")
    
frase_modificada = frase.replace(palavra_antiga, palavra_nova)
print(f"Frase modificada: {frase_modificada}")