from datetime import datetime
import pytz
from random import randint


# Nomes de Classe começar com letrar maiúscula como ex. ContaCorrete.
class ContaCorrente:

    # Atributos globais da classe, se alterar essa variável altera o valor para todas as instâncias da classe
    # cor = 'Azul'

    # O @staticmetohod serve para informar que nosso metodo não usa nenhuma informação da classe.
    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br.strftime('%d/%m/%Y %H:%M:%S')

    # Atributos de instância da classe
    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.agencia = agencia
        self.num_conta = num_conta
        self.limite_especial = 1000
        self.cartoes = []
        self.transacoes = []

    # Métodos da Classe

    def consultar_saldo(self):
        print(f'Seu saldo atual é de R${self.saldo:,.2f}')

    def depositar(self, valor):
        if valor <= 0:
            print('Não foi possível realizar o deposito.')
        else:
            self.saldo += valor

    def consultar_limite_especial(self):
        print(f'\nSeu limite de cheque especial é {abs(self.limite_especial)}\n')

    # metodo privado, apenas para uso na classe
    def _sacar_cheque_especial(self, valor):
        if valor <= 0:
            print('Não foi possível realizar o saque.')
            return False

        if valor > self.limite_especial:
            print('Limite de cheque especial insuficiente.')
            return False

        self.limite_especial -= valor
        return True

    def sacar_dinheiro(self, valor):

        if valor <= 0:
            print("Valor inválido.")
            return

        saldo_disponivel = self.saldo + self.limite_especial

        if valor > saldo_disponivel:
            print("Saldo insuficiente.")
            return

        if valor <= self.saldo:
            self.saldo -= valor

        elif valor > self.saldo:
            valor_cheque_especial = valor - self.saldo
            self.saldo = 0

            if not self._sacar_cheque_especial(valor_cheque_especial):
                return

        self.transacoes.append(
            (-valor, self.saldo, ContaCorrente._data_hora())
        )

    def consultar_transacoes(self):
        print('**** Histórico de Transações ****')

        for transacoes in self.transacoes:
            valor, saldo, date = transacoes
            print(f'Valor Sacado: {valor} | Saldo Atual: {saldo} : Data: {date}')


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_br = pytz.timezone('Brazil/East')
        horario_br = datetime.now(fuso_br)
        return horario_br

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000, 9999999999)
        self.titular = titular
        self.validade = f'{CartaoCredito._data_hora().month}/{CartaoCredito._data_hora().year + 4}'
        self.cod_seguranca = f'{randint(0, 9)}{randint(0, 9)}{randint(0, 9)}'
        self.limite = 1000
        self.conta_corrente = conta_corrente

        # Adicionando o objeto cartão dentro da lista contida na classe ContaCorrente
        conta_corrente.cartoes.append(self)


# programa
conta_Lira = ContaCorrente("Lira", "111.222.333-45", 1, 666)

cartao_Lira = CartaoCredito('Lira', conta_Lira)

print(conta_Lira.cartoes)

# Numero do cartão
print(conta_Lira.cartoes[0].numero)

print(cartao_Lira.validade)
print(cartao_Lira.cod_seguranca)
print(cartao_Lira.numero)
