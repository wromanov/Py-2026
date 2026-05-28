import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import openpyxl

agora = pd.Timestamp.now()

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)

fila_servico_cabling = pd.read_excel(r'C:\Users\walacedelgado\Downloads\Filas de Serviço.xlsx',
                                     sheet_name='Telecom 27_05_2026')

fila_servico_cabling = fila_servico_cabling.rename(columns={'#': 'OS'})

fila_servico_cabling = fila_servico_cabling[
    ['OS', 'Tipo de Registro de Serviço', 'Status', 'Usuário Solicitante', 'Responsável', 'Data de solicitação']]

# Transformando coluna em datetime
fila_servico_cabling['Data de solicitação'] = pd.to_datetime(fila_servico_cabling['Data de solicitação'], dayfirst=True,
                                                             format='%d-%m-%Y %H:%M:%S', errors='coerce')

# Criando coluna de Aging
fila_servico_cabling['Aging'] = (agora - fila_servico_cabling['Data de solicitação'])


# Função para contar quantas vezes cada valor do dataframe aparece
def verificar_valores_por_quantidade(dataframe, nome_coluna):
    return dataframe[nome_coluna].value_counts()


def calcular_aging(fila, tempo):
    return len(fila[fila_servico_cabling['Aging'].dt.days >= tempo])


quantidade_por_status = verificar_valores_por_quantidade(fila_servico_cabling, 'Status')

quantidade_por_responsavel = verificar_valores_por_quantidade(fila_servico_cabling, 'Responsável')

aging_maior_10 = calcular_aging(fila_servico_cabling, 10)

aging_maior_20 = calcular_aging(fila_servico_cabling, 20)

aging_maior_30 = calcular_aging(fila_servico_cabling, 30)

print('\n')
print(f'Quantidade total de chamados na fila "Telecom": {len(fila_servico_cabling['OS'])}')
print('\n')
print('***** Quantidade de chamados por Status *****')
print(quantidade_por_status)
print('\n')
print('***** Quantidade de chamado por responsável *****')
print(quantidade_por_responsavel)
print('\n')

# print(fila_servico_cabling)

print('***** Aging Time Chamados *****')
print(f'Chamados abertos >= 10 dias: {aging_maior_10}')
print(f'Chamados abertos >= 20 dias: {aging_maior_20}')
print(f'Chamados abertos >= 30 dias: {aging_maior_30}')


quantidade_por_responsavel.plot(kind='pie', figsize=(11, 5), autopct='%1.1f%%')
plt.show()
