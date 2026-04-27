"""
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
* salário bruto.
* quanto pagou ao INSS.
* quanto pagou ao sindicato.
* o salário líquido.
* calcule os descontos e o salário líquido, conforme a tabela abaixo:
"""

valor_hora_trabalhada = float(input('Informe o valor da hora trabalhada: '))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas: '))
percent_desconto_irpf = 0.11
percent_desconto_inss = 0.08

salario_bruto = valor_hora_trabalhada * horas_trabalhadas
salario_desconto_irpf = salario_bruto * percent_desconto_irpf
salario_desconto_inss = salario_bruto * percent_desconto_inss
salario_liquido = salario_bruto - salario_desconto_irpf - salario_desconto_inss

print(f'Salário bruto R${salario_bruto:.2f}')
print(f'Valor pago ao INSS R${salario_desconto_inss:.2f}')
print(f'Valor pagor ao IRPF R${salario_desconto_irpf:.2f}')
print(f'Salário liquido R${salario_liquido:.2f}')
