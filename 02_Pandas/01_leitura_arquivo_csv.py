import pandas as pd

#Abrindo arquivo CSV
vendas_df = pd.read_csv(
    r"C:\Users\walac\Desktop\Python_Impressionador-Hashtag-2023\22. Dados-Pandas + Python e Excel\3. Pandas e csv\Contoso - Vendas - 2017.csv", sep=";", index_col=0)

#Exibindo DateFrame
print(vendas_df)
