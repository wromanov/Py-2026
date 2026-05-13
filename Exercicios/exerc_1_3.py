# ### Terceira versão da lista de compras

# Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código.
# Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`.
# Crie também uma função para mostrar o menu. O programa deve continuar funcionando da mesma forma,
# mas agora o código deve estar organizado em funções.
#

def adicionar_item(item, quantidade, lista):
    lista.setdefault(item, quantidade)


def remover_item(item, lista):
    lista.pop(item)
    return item


def exibir_lista(lista):
    for item in lista:
        chave, valor = item
        print(f'Item: {chave} - Quantidade: {valor}')


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
            adicionar_item(item_chave, item_valor, lista_compras)
            print(f'Item {item_chave} adicionado na lista com sucesso .')

        case 2:

            print('Opção 2: Remover Item\n')
            print('***Lista de Compras!***')

            if not lista_compras:
                print('A Lista de compras está vazia!')

            elif lista_compras:
                exibir_lista(lista_compras)
                item_chave_remover = input('Informe o nome do item que deseja remover: ').capitalize().strip()

                if item_chave_remover not in lista_compras:
                    print('O item não está contido na lista de compras!')

                else:
                    item_removido = remover_item(item_chave_remover, lista_compras)
                    print(f'Item \'{item_removido}\' removido da lista de compras!.')
                    exibir_lista(lista_compras)

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
