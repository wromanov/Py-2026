"""
Exercício 08
Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

salario_hora = int(input('Valor da hora trabalhada? '))
horas_trabalhadas_mes = int(input('Quantos horas trabalhadas no mês?  '))

salario = salario_hora * horas_trabalhadas_mes

print(f'Seu salario no mês é {salario:.2f}')




