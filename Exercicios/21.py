"""
2. Análise de Vendas
Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.
Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os
vendedores que bateram a meta e qual foi o valor que eles venderam.
"""

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

for num, item in enumerate(vendas):
       if item[1] >= meta:
           print(f'funcionário {item[0]} bateu a meta e fez {item[1]} de vendas.')