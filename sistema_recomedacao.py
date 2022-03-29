import pandas as pd
import csv

#filmesFile = pd.read_csv('Filmes.csv')

with open('filmes.csv', mode='r') as arq:
    leitor = csv.reader(arq, delimiter=',')
    linhas = 0
    for coluna in leitor:
        if linhas == 0:
            linhas += 1
        else:
            print(f'{coluna[0]}, {coluna[1]}, {coluna[2]}')
            linhas+=1
