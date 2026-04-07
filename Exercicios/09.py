"""
Exercício 8 — Custo de viagem
Uma viagem de 320 km com consumo médio de 16 km/l e gasolina a R$6,20. Calcule o custo.
"""
km_viagem = 320
consumo_litros = 16
gas_preco = 6.20

fator_consumo = km_viagem / consumo_litros
valor_consumo = gas_preco * fator_consumo

print(f'O custo de abastecimento da viagem será de R$ {valor_consumo:.2f}')
