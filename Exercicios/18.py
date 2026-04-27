"""
João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.
"""

peso_peixe = int(input('Informe a quantidade de peixe em Kg: '))
peso_limite = 50
peso_excesso = 0
multa_kg_excedente = 4
total_multa = 0

if peso_peixe > peso_limite:
    peso_excesso = peso_peixe - peso_limite
    total_multa = peso_excesso * multa_kg_excedente
    print(
        f'Quantidade total de peixe {peso_peixe} kg | Excesso de peixe {peso_excesso} kg | Valor da Multa a pagar R$ {total_multa}.')
else:
    print(f'Quantidade total de peixe {peso_peixe} Kg, não há multa.')