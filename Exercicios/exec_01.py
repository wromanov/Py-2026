# Estruture seu programa da seguinte forma:
#
# 1. Crie uma lista vazia para armazenar os itens da lista de compras.
# 2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
# 3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
# 4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
# 5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
# 6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
# 7. Se o usuário escolher sair, encerre o loop usando break.
#
# Exemplo de saída:
#
# ```
# 1 Adicionar item
# 2 Remover item
# 3 Ver lista
# 4 Sair
# Escolha uma opção: 1
# Digite um item: banana


lista_compras = []

while True:
    print('*-- App Lista de Compras --**')
    opcao = int(input('Opções:\n#1 - Adcionar Item\n#2 - Remover Item\n#3 - Ver lista\n#4 - Sair\nEscolha a opção: '))

    match opcao:
        case 1:
            print('Opção 1: Adicionar Item')
            item = input('Informe o nome do item que deseja adicionar: ')
            lista_compras.append(item)
        case 2:
            print('Opção 2: Remover Item')
            item_remover = input('Informe o nome que deseja remover: ')
            if item_remover in lista_compras:
                item_indice = lista_compras.index(item_remover)
                item_removido = lista_compras.pop(item_indice)
                print(f'O item: {item_removido}, foi removido da lista.')
                print('\n')
            else:
                print(f'O item: {item_remover}, não foi encontrado na lista.')
                print('\n')
        case 3:
            print('Opção: Ver lista')
            for a, i in enumerate(lista_compras):
                print(f' Item {a}: {i}')
            print('\n')
        case 4:
            break
        case _:
            print('Opção Invalida!')