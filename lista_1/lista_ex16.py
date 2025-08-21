#contar palavras de uma frase

def contar_palavras(frase):
    palavras = frase.split() 
    return len(palavras)      

texto_usuario = input("Digite uma frase: ")
quantidade_palavras = contar_palavras(texto_usuario)
print(f"A frase contém {quantidade_palavras} palavras.")