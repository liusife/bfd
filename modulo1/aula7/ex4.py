import conversao as conv

escolha = input("Digite 'C' para converter de Fahrenheit para Celsius ou 'F' para converter de Celsius para Fahrenheit: ").upper()
temperatura = float(input("Digite a temperatura a ser convertida: "))

if escolha == 'C':
    resultado = conv.fahrenheit_para_celsius(temperatura)
    print(f"{temperatura}°F é igual a {resultado:.2f}°C")
elif escolha == 'F':
    resultado = conv.celsius_para_fahrenheit(temperatura)
    print(f"{temperatura}°C é igual a {resultado:.2f}°F")