meta = 50000
qtd_vendida = 5500

if qtd_vendida > meta:
    print(f'Meta batida {qtd_vendida} unidades vendidas.')
else:
    print(f'A Meta não foi batida {qtd_vendida} unidades vendidas.')
print('Fim do programa.')

# Exemplo
"""Vamos fazer um novo exemplo abaixo:
Digamos que você precisa criar um programa para um fundo de investimentos conseguir avaliar o resultado de uma carteira de ações e o quanto de taxa deverá ser pago.

A regra desse fundo de investimentos é:

- O fundo se compromete a entregar no mínimo 5% de retorno ao ano.
- Caso o fundo não consiga entregar os 5% de retorno, ele não pode cobrar taxa dos seus investidores.
- Caso o fundo consiga entregar mais de 5% de retorno, ele irá cobrar 2% de taxa dos seus investidores.
- Caso o fundo consiga mais de 20% de retorno, ele irá cobrar 4% de taxa dos seus investidores."""

eta = 0.05
taxa = 0
rendimento = 0.25

if rendimento > meta:
    if rendimento > 0.20:
        taxa = 0.04
        print(f'A taxa foi de {taxa}')
    else:
        taxa = 0.02
        print(f'A taxa foi de {taxa}')
else:
    taxa = 0
    print(f'A taxa foi de {taxa}')

