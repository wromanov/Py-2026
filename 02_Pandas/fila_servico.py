import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

agora = pd.Timestamp.now()

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)

fila_servico_cabling = pd.read_csv('export.csv', sep=',')

fila_servico_cabling = fila_servico_cabling.rename(columns={'#': 'OS'})

fila_servico_cabling = fila_servico_cabling[
    ['OS', 'Tipo de Registro de Serviço', 'Status', 'Usuário Solicitante', 'Responsável', 'Data de solicitação']]

# Transformando coluna em datetime
fila_servico_cabling['Data de solicitação'] = pd.to_datetime(fila_servico_cabling['Data de solicitação'], dayfirst=True, format='%d-%m-%Y %H:%M:%S', errors='coerce')

# Criando coluna de Aging
fila_servico_cabling['Aging'] = (agora - fila_servico_cabling['Data de solicitação'])


# Função para contar quantas vezes cada valor do dataframe aparece
def verificar_valores_por_quantidade(dataframe, nome_coluna):
    return dataframe[nome_coluna].value_counts()


quantidade_por_status = verificar_valores_por_quantidade(fila_servico_cabling, 'Status')
quantidade_por_responsavel = verificar_valores_por_quantidade(fila_servico_cabling, 'Responsável')

print('\n')
print(f'Total de chamados na fila: {len(fila_servico_cabling['OS'])}')
print('\n')
print(quantidade_por_status)
print('\n')
print(quantidade_por_responsavel)
print('\n')
# quantidade_por_responsavel.plot(kind='pie', figsize=(12, 10), autopct='%1.1f%%')
# plt.show()

print(fila_servico_cabling)

vencidos = len(
    fila_servico_cabling[
        fila_servico_cabling['Aging'].dt.days >= 10
    ]
)

print(vencidos)
print('\n')
