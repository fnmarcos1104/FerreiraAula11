import os 

os.system('cls')

import pandas as pd

try:
    df = pd.read_csv('ClassicDisco.csv', sep=',', encoding='utf-8')
    # print(df) #IMPRIME INICIO E FIM
    # print(df.to_string()) #IMPRIME TUDO
    # print(df.head(10)) #IMPRIME QUANTIDADE SELECIONADA
    # print(df.tail()) #IMPRIME O FIM
    # print(df.info()) #IMPRIME INFORMAÇÕES
    # print(df.describe()) #IMPRIME RESUMO DA BASE DE DADOS

    # pd.set_option('display.min_rows', 5) #IMPRIME QUANTIDADE DE LINHAS ESCOLHIDA
    # print(df)

    # artistas = df ['Track'] #LENDO UMA COLUNA ESPECÍFICA
    # print(artistas.to_string())

    # popularidade = df[df['Popularity'] > 20] #FILTRAGEM DE DADOS
    # print(popularidade.to_string())
    # print(popularidade[['Track', 'Popularity']])

    # michael_jackson = df[df['Artist'] == 'Michael Jackson'] #IMPRIME LINHA COM CONTEÚDO ESPECÍFICO
    # print(michael_jackson[['Album', 'Artist']])

    # pd.set_option('display.max_columns', None) #Exibir todas as colunas
    
    # pd.set_option('display.max_columns', None) #Exibir 

    df.to_csv('Base_modificada.cvs', index=False, sep=',', encoding='utf-8')
    df.to_excel('classic_disco_modificado.xls', index=False, engine='openpyxl')



except Exception as e:
    print(f'Erro {e}')
    exit()