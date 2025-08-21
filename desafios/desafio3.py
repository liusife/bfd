nome_usuario = input("Digite seu nome: ")
numero_usuario = input("Digite o seu número de Whatsapp: ")
peso_usuario = float(input("Digite o seu peso (Kg): "))
altura_usuario = float(input("Digite a sua altura em metros: "))

imc = round(peso_usuario / (altura_usuario * altura_usuario), 2)
consumo_agua = ((35 * peso_usuario) / 1000)
print(f" Nome: {nome_usuario}\n Whatsapp: {numero_usuario}\n IMC: {imc}\n Consumo diário de água: {consumo_agua} litros")