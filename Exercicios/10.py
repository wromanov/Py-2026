"""
Exercício 9 — Cadastro de colaborador
Cadastre nome, idade, cargo e salário e exiba formatado.
"""

nome = input('Qual o seu nome? ').strip()
idade = int(input('Qual a sua idade? '))
cargo = input('Qual a sua cargo? ')
salario = float(input('Qual o seu salario? '))

print(f"Nome: {nome}, idade: {idade}, cargo: {cargo}, salario: {salario}.")