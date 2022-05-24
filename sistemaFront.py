import csv
from pywebio import *
from pywebio.input import TEXT, FLOAT
from pywebio.output import *
from sistema_recomedacao import *

Users = []
Movie_list = []

def addNewUser():
    new_user = input.input("Nome do usuário：", type=TEXT)
    if new_user in Users:
        return new_user
    else:
        Users.append(new_user)
        with open('usuarios.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for user in Users:    
                writer.writerow([user])
    return new_user

with open('usuarios.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter=',')
    for coluna in leitor:
        Users.append(coluna[0])

with open('filmes.csv', mode='r', encoding='utf-8') as arq:
    leitor = csv.reader(arq, delimiter=',')
    for coluna in leitor:
        Movie_list.append(coluna[0])

def limite_nota(nota):
    if nota < 0 or nota > 5:
        return "Valor inválido"

def main():  # PyWebIO application function
    username = addNewUser()
    # username = input.select('Selecionar Usuário', Users)
    movie = input.select('Escolha um filme para avaliar', Movie_list)
    # nota = input.select('Qual nota você dá para esse filme?', [0, 1, 2, 3, 4, 5])
    nota = input.input('Qual nota você dá para esse filme? (Entre 0 e 5)', type=FLOAT, validate=limite_nota)
    lista = MovieRec(username, movie, nota)

    put_markdown(r""" # 🎥MovieRec """)
    put_text("Protótipo de Sistema de Recomendação de filmes")
    put_markdown(r"""# Olá %s, talvez você goste desses filmes:""" % (username),)

    put_row([
        put_table(lista[0]),
        put_table(lista[1])
    ])
if __name__ == '__main__':
    start_server(main, port=80)