import os

os.system('cls')


import pandas as pd

# [1] DF DE 3 COLUNAS FILME, ANO DE LANÇAMENTO E GENERO

dados = {
    'filmes' : ['Homem Aranha', 'Intocávéis', 'Operação Baba'],
    'ano' : [2002, 2010, 2014],
    'genero' : ['Ação', 'Drama', 'Comédia']
}


df = pd.DataFrame(dados)
print(df)
print(30*'=')

serie_colunas = df.loc[:,'filmes']
print('\n',serie_colunas)
print(30*'=')

series_linha = df.iloc[2]
print('\n', series_linha)

