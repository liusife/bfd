valor_hora_trabalhada = int(input("Informe o valor recebido por hora trabalhada: "))
quant_hora_mes = int(input("Infome a quantidade de horas trabalhadas no mês: "))

salario_bruto = (valor_hora_trabalhada * quant_hora_mes)
desc_ir = (salario_bruto * (11/100))
desc_inss = (salario_bruto * (8/100))
desc_sind = (salario_bruto * (5/100))

salario_liq = (salario_bruto - (desc_ir) - (desc_inss) - (desc_sind))

print(f"+ Salário Bruto: R${salario_bruto:.2f} \n- IR (11%): R${desc_ir:.2f} \n- INSS (8%): R${desc_inss:.2f} \n- Sindicato(5%): R${desc_sind:.2f} \n= Salário Líquido: R${salario_liq:.2f}")
