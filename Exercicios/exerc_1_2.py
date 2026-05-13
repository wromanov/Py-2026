# ### Segunda versão da lista de compras
#

# Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
# O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
# adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
# deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
# se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
# e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.
#
# O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.
#
# Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
# usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
# deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
# mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
# "Maçã" e "maçã" devem ser considerados o mesmo item.


lista_compras = {}

while True:
    print('\n*-- App Lista de Compras --**')

    try:
        opcao = int(input('Opções:\n'
                          '#1 - Adicionar Item\n'
                          '#2 - Remover Item\n'
                          '#3 - Ver lista\n'
                          '#4 - Sair\n'
                          'Escolha a opção: '))

    except ValueError:
        print('\nDigite apenas números.')
        # Quebra o fluxo e volta para o while.
        continue

    match opcao:

        case 1:

            print('Opção 1: Adicionar Item')
            item_chave = input('Informe o nome do item que deseja adicionar: ').capitalize().strip()
            item_valor = input('Informe a quantidade de items que deseja adicionar: ')
            lista_compras.setdefault(item_chave, item_valor)
            print(f'Item {item_chave} adicionado na lista com sucesso .')

        case 2:

            print('Opção 2: Remover Item\n')
            print('***Lista de Compras!***')

            if not lista_compras:
                print('A Lista de compras está vazia!')

            elif lista_compras:
                print(lista_compras)
                item_chave_remover = input('Informe o nome do item que deseja remover: ').capitalize().strip()

                if item_chave_remover not in lista_compras:
                    print('O item não está contido na lista de compras!')

                else:
                    item_removido = lista_compras.pop(item_chave_remover)
                    print(f'Item removido {item_removido} da lista de compras!.')
                    print(lista_compras)

        case 3:

            print('Opção: Ver lista')
            for chave, valor in lista_compras.items():
                print(f' Item: {chave} - Quantidade: {valor}.')
            print('\n')

        case 4:

            print('Saindo...')

            break

        case _:

            print('Opção Invalida!')
