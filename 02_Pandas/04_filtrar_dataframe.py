import pandas as pd

# importando os arquivos
vendas_df = pd.read_csv(r'Contoso - Vendas - 2017.csv', sep=';', encoding='cp1252')
produtos_df = pd.read_csv(r'Contoso - Cadastro Produtos.csv', sep=';', encoding='cp1252')
lojas_df = pd.read_csv(r'Contoso - Lojas.csv', sep=';', encoding='cp1252')
clientes_df = pd.read_csv(r'Contoso - Clientes.csv', sep=';', encoding='cp1252')

# Renomear nome da coluna
clientes_df = clientes_df.rename(columns={'ÿID Cliente': 'ID Cliente'})
produtos_df = produtos_df.rename(columns={'ÿNome do Produto': 'Nome do Produto'})
lojas_df = lojas_df.rename(columns={'ÿID Loja': 'ID Loja'})

# limpando apenas as colunas que queremos
clientes_df = clientes_df[['ID Cliente', 'E-mail']]
produtos_df = produtos_df[['ID Produto', 'Nome do Produto']]
lojas_df = lojas_df[['ID Loja', 'Nome da Loja']]

# mesclando e renomeando os dataframes
vendas_df = vendas_df.merge(produtos_df, on='ID Produto')
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
vendas_df = vendas_df.merge(clientes_df, on='ID Cliente').rename(columns={'E-mail': 'E-mail do Cliente'})

## Primeiro, vamos aplicar uma função normalmente. Qual o % das vendas que foi devolvido?
# Para isso vamos somar as quantidades nas colunas correspondentes. Lembrando, o % vai ser: Total Devolvido / Total Vendido.

qtde_vendida = vendas_df['Quantidade Vendida'].sum()
qtde_devolvida = vendas_df['Quantidade Devolvida'].sum()

print(f'{qtde_devolvida / qtde_vendida:.2%}')

## Agora, se quisermos fazer a mesma análise apenas para 1 loja. Queremos filtrar apenas os itens da Loja Contoso Europe Online e saber o % de devolução dessa loja.
# - Para isso, vamos precisar filtrar. A forma de filtrar nos dataframes é uma "simples" comparação

vendas_lojacontosoeuropeonline = vendas_df[vendas_df['ID Loja'] == 306]
qtde_vendida = vendas_lojacontosoeuropeonline['Quantidade Vendida'].sum()
qtde_devolvida = vendas_lojacontosoeuropeonline['Quantidade Devolvida'].sum()

print(f'{qtde_devolvida / qtde_vendida:.2%}')

## Desafio: e se eu quisesse criar uma tabela apenas com as vendas da Loja Contoso Europe Online e que não tiveram nenhuma devolução. Quero criar essa tabela e saber quantas vendas são.
# Repare que nesse caso são 2 condições, como fazemos isso?

#tudo junto
df_loja306semdev = vendas_df[(vendas_df['ID Loja'] == 306) & (vendas_df['Quantidade Devolvida'] == 0)]

print(df_loja306semdev)

#separado
loja306 = vendas_df['ID Loja'] == 306
qtde_devolvida_0 = vendas_df['Quantidade Devolvida'] == 0
df2_loja306semdev = vendas_df[loja306 & qtde_devolvida_0]

print(df2_loja306semdev)

