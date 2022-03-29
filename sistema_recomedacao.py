import pandas as pd
import csv

with open('filmes.csv', mode='r') as arq:
    leitor = csv.reader(arq, delimiter=',')
    linhas = 0
    for coluna in leitor:
        if linhas == 0:
            linhas += 1
        else:
            print(f'{coluna[0]}')
            linhas += 1

# filmesFile = pd.read_csv('filmes.csv', delimiter='')

# lines = 0
# for filme in filmesFile:
#     print(filme)

# print(filmesFile)
