# ## Relatório de vendas
from traceback import print_tb

# ### Primeira versão do relatório de vendas

# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
# O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
# do total e da média de vendas para cada vendedor.
#
# Estruture seu programa da seguinte forma:
#
# 1. Crie um dicionário vazio para armazenar os dados de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
#

lista_vendas = {}

nome = input("Digite o nome do vendedor: ")
qtd_venda = int(input("Digite a quantidade de vendas: "))

# verifica se já existe na lista
if nome in lista_vendas:
    lista_vendas[nome]['total_vendas'] += qtd_venda
    lista_vendas[nome]['quantidade_vendas'] += 1

else:
    lista_vendas[nome] = {'total_vendas': qtd_venda, 'quantidade_vendas': 1}

for vendedor, dados in lista_vendas.items():
    print(f'{vendedor}')
    print(dados['total_vendas'])
    print(dados['quantidade_vendas'])



