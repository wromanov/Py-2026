lista_alunos1 = {
    "João": 4.5,
    "Maria": 5.0,
    "Carlos": 3.8,
    "Ana": 7.2,
    "Pedro": 2.5,
    "Juliana": 8.0,
    "Rafael": 6.5,
    "Fernanda": 1.9,
    "Lucas": 10.0,
    "Camila": 5.7
}


# for alunos in lista_alunos:
#    print(lista_alunos[alunos])


def aprovados(lista_alunos, nota_aprovacao):
    alunos_aprovados = ()
    for aluno in lista_alunos:
        if lista_alunos[aluno] >= nota_aprovacao:
            alunos_aprovados += (aluno, lista_alunos[aluno])
    return alunos_aprovados


alunos_aprovados = aprovados(lista_alunos1, 6)
print(alunos_aprovados)
