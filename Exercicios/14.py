"""
Exercício 16 — Domínio de e-mail
Extraia o domínio de 'usuario@empresa.com'
"""
email = "walacecastro@live.com"
caractere = email.find("@")
dominio = email[caractere:]
print(dominio)
