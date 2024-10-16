import os

os.system('cls')


import pandas as pd

dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente', 'auxiliar'],
    'salário': [2500, 1800, 750, 1900]
}
# EXE_01
# print(dados)
# print(type(dados))

# EXE_02
df = pd.DataFrame(dados)
# print(df)

# EXE_03
serie_cargos = pd.Series(df['cargos'])
# print(serie_cargos)

# EXE_04
serie_salarios = pd.Series(df['salário'])
# print(serie_salarios)
# print(type(serie_salarios))

# EXE_05
# print(serie_cargos.index)
# print(serie_cargos.values)

# EXE_06
print(df,'\n')
serie_linha = df.iloc[1]
# print(serie_linha)

# EXE_07
# serie_colunas = df.loc[:,'cargos']
# print(serie_colunas)

# EXE_07.2
# df.index = ['A', 'B', 'C']
# serie_colunas = df.loc['A']
# print(serie_colunas, '\n')

# EXE_08
# print(serie_cargos.iloc[0])
# print(serie_cargos[serie_cargos.index[0]])
# print(df.iloc[0])

# EXE_09
# print(df[df['cargos'] == 'auxiliar'])
salarios = df.loc[df['cargos'] == 'auxiliar', 'salário']
print(salarios)