import csv
from pywebio import *
from pywebio.output import *
from sistema_recomedacao import *

Users = []

with open('usuarios.csv', mode='r') as arq:
    leitor = csv.reader(arq, delimiter=',')
    for coluna in leitor:
        Users.append(coluna[0])

def main():  # PyWebIO application function

    put_markdown(r""" # 🎥MovieRec """)
    put_text("Protótipo de Sistema de Recomendação de filmes")

    username = input.select('Selecionar Usuário', Users)
    lista = MovieRec(username)

    put_table([
    ['Recomendações', 'Vizinhos'],
    ])

    put_table(lista)
    # put_table([
    # ['Type', 'Content'],
    # ['html', put_html('X<sup>2</sup>')],
    # ['text', '<hr/>'],  # equal to ['text', put_text('<hr/>')]
    # ['buttons', put_buttons(['Recomendados'], onclick=...)],  
    # ['markdown', put_markdown('`Awesome PyWebIO!`')],
    # ['file', put_file('hello.text', b'hello world')],
    # ['table', put_table([['A', 'B'], ['C', 'D']])]
    # ])

if __name__ == '__main__':
    start_server(main, port=80)