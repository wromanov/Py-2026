# Operadores Lógicos em Python
# Python possui três operadores lógicos principais: and, or, e not. Eles são usados para combinar expressões booleanas e controlar o fluxo do programa.

# and (E lógico)
# Retorna True apenas se TODAS as condições forem verdadeiras.

idade = 25
possui_carteira = True

# Verifica se a pessoa pode dirigir
if idade >= 18 and possui_carteira:
    print("Pode dirigir!")  # Executa porque ambas são True

# Exemplos práticos
numero = 15
if numero > 10 and numero < 20:
    print("Número está entre 10 e 20")  # True

# Com strings
usuario = "admin"
senha = "1234"
if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")  # Executa

    # Short-circuit evaluation (avaliação de curto-circuito)
    # Se a primeira condição for False, a segunda nem é avaliada
    x = 5
    if x < 0 and (10 / x) > 1:  # (10/x) NÃO é executado porque x<0 é False
        print("Isso não causa erro de divisão por zero")


# or (OU lógico)
# Retorna True se PELO MENOS UMA das condições for verdadeira.

dia = "sábado"

# Verifica se é fim de semana
if dia == "sábado" or dia == "domingo":
    print("É fim de semana!")  # Executa

# Exemplos práticos
temperatura = 35
if temperatura < 10 or temperatura > 30:
    print("Temperatura extrema!")  # Executa (35 > 30)

# Validação de entrada
nome = input("Digite seu nome: ")
if nome == "" or nome is None:
    print("Nome não pode ser vazio!")

# Short-circuit evaluation
# Se a primeira condição for True, a segunda nem é avaliada
x = 10
if x > 0 or (10 / x) > 5:  # (10/x) NÃO é executado porque x>0 é True
    print("X é positivo")