"""
Exercícios
1. Criando um Registro de Hóspedes
Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel.
No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:
1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:

"""

qtd_hospedes = int(input('Informa a quantidade de hospedes: '))
quarto = []
for c in range(qtd_hospedes):
    nome = input(f'Informe o nome do {c+1}º hospede: ')
    cpf = input(f'Informe o cpf do {c+1}º hospede: ')
    hospede = [nome, f'cpf:{cpf}']
    quarto.append(hospede)

for hospede in quarto:
    print(hospede)

