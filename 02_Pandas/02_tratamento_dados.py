import pandas as pd
from pandas._libs import join
from pandas.tseries import holiday

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', None)

# Às vezes precisaremos mudar o encoding. Possíveis valores para testar:
# encoding='latin1', encoding='ISO-8859-1', encoding='utf-8' ou então encoding='cp1252'
# vendas_df = pd.read_csv(r'Contoso - Vendas  - 2017.csv', sep=';')


vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';', encoding='cp1252')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';', encoding='cp1252')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';', encoding='cp1252')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';', encoding='cp1252')

# Renomear nome da coluna
clientes_df = clientes_df.rename(columns={'ÿID Cliente': 'ID Cliente'})
produtos_df = produtos_df.rename(columns={'ÿNome do Produto': 'Nome do Produto'})
lojas_df = lojas_df.rename(columns={'ÿID Loja': 'ID Loja'})

# selecionando apenas colunas que serão utilizadas
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# Relacionado os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente')

print(vendas_df)
