# Inteiro → int
# Usado para números inteiros, sem casas decimais.
idade = 30
ano = 2026
temperatura = -5
print(type(idade), type(idade), type(temperatura))

# Decimal → float
# Usado para números com ponto decimal.
altura = 1.75
preco = 99.90
nota = 8.5
print(type(altura))

# Texto → str
# Usado para textos e caracteres.
nome = "Walace"
cidade = "Rio de Janeiro"
letra = "A"
print(type(nome))

# Booleano → bool
# Usado para verdadeiro ou falso.
ligado = True
desligado = False
print(type(ligado))

# Lista → list
# Usada para armazenar vários valores.
nomes = ["Ana", "Carlos", "Walace"]
numeros = [1, 2, 3, 4]
print(type(nomes))

# Tupla → tuple
# Parecida com lista, mas não pode ser alterada.
coordenadas = (10, 20)
print(type(coordenadas))

# Dicionário → dict
# Armazena valores em pares chave: valor.
pessoa = {
    "nome": "Walace",
    "idade": 30
}
print(type(pessoa))

# Conjunto → set
# Armazena valores únicos, sem repetição.
numeros = {1, 2, 3, 3, 4}
print(numeros)

# Nulo / vazio → NoneType
# Representa ausência de valor.
resultado = None
print(type(resultado))