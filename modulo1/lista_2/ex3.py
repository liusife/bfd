#ingressos show

pessoas = []

qnt_ingressos = int(input("Quantidade de ingressos: "))

for i in range(qnt_ingressos):
    nome = input(f"Nome da pessoa do {i+1}º ingresso: ")
    idade = int(input(f"Idade de {nome}: "))

