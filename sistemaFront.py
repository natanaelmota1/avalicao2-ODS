import csv
from pywebio import *
from pywebio.output import *
from sistema_recomedacao import *

Users = []

with open('usuarios.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter=',')
    for coluna in leitor:
        Users.append(coluna[0])

def main():  # PyWebIO application function
    username = input.select('Selecionar Usuário', Users)
    lista = MovieRec(username)

    put_markdown(r""" # 🎥MovieRec """)
    put_text("Protótipo de Sistema de Recomendação de filmes")
    put_markdown('Olá %s , Talvez vc goste:' % (username),)

    put_row([
        put_table(lista[0]),
        put_table(lista[1])
    ])
if __name__ == '__main__':
    start_server(main, port=80)