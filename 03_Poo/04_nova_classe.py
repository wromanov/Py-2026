from random import randint


class Agencia:
    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.caixa = 0
        self.emprestimos = []
        self.clientes = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'Caixa abaixo do nível recomendado. Caixa Atual: R$ {self.caixa}')
        else:
            print(f'O valor de caixa está Ok. Caixa atual: R$ {self.caixa}')

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


# Criando subclasses (Herança)

class AgenciaVirtual(Agencia):
    # criando o init da classe
    def __init__(self, site, telefone, cnpj, numero):
        # incluindo o init da classe pai na subclasse
        super().__init__(telefone, cnpj, numero)
        self.site = site
        self.caixa = 1000000


class AgenciaComum(Agencia):
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(10000, 99999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    ...


# programa

agencia_01 = Agencia(21996932687, 151284, 123456)
agencia_01.caixa = 1000000

agencia_01.verificar_caixa()

agencia_01.emprestar_dinheiro(1500, 151507, 0.02)

agencia_01.adicionar_cliente('Walace', 151284, 100000)

print(agencia_01.clientes)

agencia_virtual = AgenciaVirtual('www.sourico.com', 2126991819, 151247, 789456123)

agencia_virtual.verificar_caixa()

