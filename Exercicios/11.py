"""
Exercício 10 — Login automático
Gere um login usando nome e sobrenome em letras minúsculas.
"""
nome = input('Qual o seu nome? ').strip().split()
login = "".join(nome).casefold()
print(f"Seu login é {login}.")

