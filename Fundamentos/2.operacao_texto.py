#Verificar se um nome está dentro de outro
print('W' in 'Walace')

# Comparação - Podemos comparar strings.
print("python" == "Python")

#Pegar informação do usuário
#nome = input("Qual é seu nome? ")
#print('Seu nome é ', nome)

#Concatenação +
nome = "Walace "
sobrenome = "Castro"

resultado = nome + sobrenome
print(resultado)

#Repetição *
texto = "Python "
print(texto * 3)

# Acessar caracteres por índice []
palavra = "Python"
print(palavra[0])
print(palavra[1])
print(palavra[2])

# Acessar caracteres por índice [] Negativo -
palavra = "Python"
print(palavra[-1])
print(palavra[-2])

# Fatiamento (slice) [:]

"""
# Índices positivos:   0    1    2    3    4    5
#                     [P]  [Y]  [T]  [H]  [O]  [N]
# Índices negativos:  -6   -5   -4   -3   -2   -1

print(texto[0:-1])    # "PYTHO" (do início ao penúltimo)
print(texto[0:-1:2])  # "PTO"  (índices: 0, 2, 4)
"""

palavra = "Python é vida"

#Ele pega do índice 0 até antes do 3.
print(palavra[0:3])

#[inicio:fim:passo]
print(palavra[0::2])

#Operadores de Comparação
a = "Python"
b = "Python"
c = "Py"

print(a == b)      # True  - igual
print(a != b)      # False - diferente
print(a > c)       # True  - maior (ordem lexicográfica)
print(a < c)       # False - menor
print(a >= b)      # True  - maior ou igual
print(a <= b)      # True  - menor ou igual


#Operadores de Associação (Membership)
texto = "Python Programming"

# in - está contido
print("Python" in texto)        # True
print("Java" in texto)          # False

# not in - NÃO está contido
print("Java" not in texto)      # True
print("Python" not in texto)    # False

# Funciona com listas, tuplas, dicionários, etc.
lista = [1, 2, 3, 4, 5]
print(3 in lista)               # True
print(10 not in lista)          # True

# Em dicionários, verifica as CHAVES
dicionario = {"nome": "João", "idade": 30}
print("nome" in dicionario)     # True
print("João" in dicionario)     # False (verifica chaves, não valores)
print("João" in dicionario.values())  # True (para ver valores)


#Operadores de Identidade
# is - verifica se duas variáveis referenciam o MESMO objeto
# is not - verifica se são objetos DIFERENTES

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)       # False (são listas diferentes, mesmo com mesmo conteúdo)
print(a is c)       # True  (apontam para o mesmo objeto)
print(a is not b)   # True  (são objetos diferentes)

# Cuidado com strings (Python pode otimizar)
x = "Python"
y = "Python"
print(x is y)       # Pode ser True (por causa do interning de strings)

# Métodos Específicos para Strings
texto = "Python Programming"

# startswith() - começa com
print(texto.startswith("Py"))     # True
print(texto.startswith("Java"))   # False

# endswith() - termina com
print(texto.endswith("ing"))      # True
print(texto.endswith("python"))   # False

# find() - encontra posição (retorna -1 se não encontrar)
print(texto.find("Pro"))          # 7
print(texto.find("Java"))         # -1

# index() - igual find, mas gera erro se não encontrar
print(texto.index("Pro"))         # 7
# print(texto.index("Java"))      # ValueError!

# count() - conta ocorrências
print(texto.count("p"))           # 2 (Python tem 'P' maiúsculo e 'p' minúsculo)
print(texto.lower().count("p"))   # 3 (convertendo tudo para minúsculo)

# isalpha(), isdigit(), isalnum(), etc.
print("Python123".isalnum())      # True (letras e números)
print("Python".isalpha())         # True (só letras)
print("123".isdigit())            # True (só dígitos)
print("   ".isspace())            # True (só espaços)