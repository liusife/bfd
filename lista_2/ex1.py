#torneio de futebol

gols_ros = []
gols_adv = []

vitorias = 0
empates = 0
derrotas = 0

contador = 0

while contador < 5:
    contador += 1
    print(f"\nPartida {contador}")

    sel_ros = int(input("Digite o placar da seleção Rosariense: "))
    adv = int(input("Digite o placar do adversário: "))

    gols_ros.append(sel_ros)
    gols_adv.append(adv)

for i in range(5):
    print(f"\nPartida {i+1}  \nGols da seleção no jogo {i+1}: {gols_ros[i]}  \nGols do adversário no jogo {i+1}: {gols_adv[i]}")
    
    if gols_ros[i] > gols_adv[i]:
        vitorias += 1
    elif gols_ros[i] < gols_adv[i]:
        derrotas += 1
    else:
        empates += 1

print("=== Torneio de Futebol - Seleção Rosariense ===")
print(f"Total de vitórias: {vitorias}")
print(f"Total de empates: {empates}")
print(f"Total de derrotas: {derrotas}")

