import pandas as pd

# ========================================================
# CONFIGURAÇÕES ÚTEIS PARA CONSOLE
# ========================================================

# Mostrar TODAS colunas
pd.set_option('display.max_columns', None)

# Mostra TODAS as linhas
# pd.set_option('display.max_rows', None)

# Aumenta largura horizontal do console, evitando quebra de linhas
pd.set_option('display.width', 2000)

# Impede o Pandas de quebrar colunas em várias linhas.
pd.set_option('display.expand_frame_repr', False)

# Mostrar conteúdo completo da célula
pd.set_option('display.max_colwidth', None)

# Controla casas decimais
pd.set_option('display.precision', 2)

# ========================================================
# 1. LEITURA DE ARQUIVOS
# ========================================================


# ========================================================
# LEITURA DE ARQUIVOS
# ========================================================

# Lendo arquivo CSV
vendas_df = pd.read_csv(
    r"C:\Users\walac\Desktop\Python_Impressionador-Hashtag-2023\22. Dados-Pandas + Python e Excel\3. Pandas e csv\Contoso - Vendas - 2017.csv",
    sep=";", index_col=0)

# Excel
# vendas_df = pd.read_excel(
#     'arquivo.xlsx',
#     sheet_name='Plan1'
# )

# ========================================================
# VISUALIZAÇÃO
# ========================================================

# Primeiras linhas
vendas_df.head()

# Primeiras 10 linhas
vendas_df.head(10)

# Últimas linhas
vendas_df.tail()

# Linha completa transposta (MUITO útil)
vendas_df[:1].T

# Informações do DataFrame
vendas_df.info()

# Nome das colunas
vendas_df.columns

# Quantidade de linhas e colunas
vendas_df.shape

# Tipos das colunas
vendas_df.dtypes

# Estatísticas
vendas_df.describe()

# Estatísticas incluindo texto
vendas_df.describe(include='all')

# ========================================================
# FILTROS
# ========================================================

# Filtro simples
vendas_df[vendas_df['Status'] == 'Aberto']

# Filtro maior que
vendas_df[vendas_df['Valor'] > 1000]

# Múltiplos filtros
vendas_df[
    (vendas_df['Status'] == 'Aberto') &
    (vendas_df['SLA'] == 'Vencido')
    ]

# Query (mais limpo)
vendas_df.query("Status == 'Aberto'")

# ========================================================
# CONTAGEM E AGRUPAMENTO
# ========================================================

# Contagem de valores
vendas_df['Status'].value_counts()

# Contagem em porcentagem
vendas_df['Status'].value_counts(normalize=True)

# Agrupar e contar
vendas_df.groupby('Tecnico').count()

# Agrupar e somar
vendas_df.groupby('Tecnico')['Horas'].sum()

# Agrupar e média
vendas_df.groupby('Tecnico')['Horas'].mean()

# Agrupar e ordenar
vendas_df.groupby(
    'Tecnico'
)['Horas'].sum().sort_values(
    ascending=False
)

# ========================================================
# ORDENAÇÃO
# ========================================================

# Ordem crescente
vendas_df.sort_values('Salario')

# Ordem decrescente
vendas_df.sort_values(
    'Salario',
    ascending=False
)

# ========================================================
# SELEÇÃO DE DADOS
# ========================================================

# Linha específica
vendas_df.loc[0]

# Coluna específica
vendas_df.loc[:, 'Nome']

# Linha e coluna
vendas_df.loc[0, 'Nome']

# Seleção por índice numérico
vendas_df.iloc[0]

# Linha e coluna por índice
vendas_df.iloc[0, 2]

# ========================================================
# VALORES NULOS
# ========================================================

# Verificar nulos
vendas_df.isnull()

# Contar nulos
vendas_df.isnull().sum()

# Preencher nulos
vendas_df.fillna(0)

# Preencher texto
vendas_df.fillna('Sem informação')

# Remover nulos
vendas_df.dropna()

# Remover colunas com nulos
vendas_df.dropna(axis=1)

# ========================================================
# VALORES ÚNICOS
# ========================================================

# Valores únicos
vendas_df['Status'].unique()

# Quantidade valores únicos
vendas_df['Status'].nunique()

# ========================================================
# ALTERAÇÃO DE DADOS
# ========================================================

# Renomear coluna
vendas_df.rename(
    columns={'Status': 'Estado'}
)

# Remover coluna
vendas_df.drop(columns=['Status'])

# Remover linha
vendas_df.drop(index=0)

# Converter tipo
vendas_df['ID'] = vendas_df[
    'ID'
].astype(int)

# ========================================================
# DUPLICADOS
# ========================================================

# Verificar duplicados
vendas_df.duplicated()

# Contar duplicados
vendas_df.duplicated().sum()

# Remover duplicados
vendas_df.drop_duplicates()

# ========================================================
# AMOSTRAGEM
# ========================================================

# Linhas aleatórias
vendas_df.sample(5)

# ========================================================
# EXPORTAÇÃO
# ========================================================

# Exportar Excel
vendas_df.to_excel(
    'resultado.xlsx',
    index=False
)

# Exportar CSV
vendas_df.to_csv(
    'resultado.csv',
    index=False
)

# ========================================================
# COMANDOS MAIS IMPORTANTES PARA ITSM / SYSAID
# ========================================================

# Quantidade por status
vendas_df['Status'].value_counts()

# Chamados SLA vencido
vendas_df[
    vendas_df['SLA'] == 'Vencido'
    ]

# Chamados por técnico
vendas_df.groupby(
    'Tecnico'
).count()

# Chamados abertos
vendas_df[
    vendas_df['Status'] == 'Aberto'
    ]

# Exportar relatório
vendas_df.to_excel(
    'relatorio.xlsx',
    index=False
)

# ========================================================
# FIM
# ========================================================
