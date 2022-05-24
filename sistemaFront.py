import csv
from pywebio import *
from pywebio.input import TEXT, FLOAT, input_group
from pywebio.output import *
from sistema_recomedacao import *
from pywebio.session import run_js

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
    if nota < 0 or nota > 10:
        return "Valor inválido"

def main():  # PyWebIO application function
    
    #geradorAvaliacoes() #-- usado para inicializar um json de usuários e notas
    
    username = addNewUser()
    movies = []
    notas = []
    for i in range(5):
        movieNota = input_group("Avaliação de Filme",[
            input.select('Escolha um filme para avaliar', Movie_list, name="movie"),
            input.input('Qual nota você dá para esse filme? (0 a 10)', type=FLOAT, validate=limite_nota, name="nota")
            ])
        movie = movieNota["movie"]
        nota = movieNota["nota"]
        movies.append(movie)
        notas.append(nota)
    
    lista = MovieRec(username, movies, notas)

    put_markdown(r""" # 🎥MovieRec """)
    put_text("Protótipo de Sistema de Recomendação de filmes")
    put_markdown(r"""# Olá %s, talvez você goste desses filmes:""" % (username),)

    put_row([
        put_table(lista[0]),
        put_table(lista[1])
    ])
    put_button("Reload", onclick=lambda: run_js('window.location.reload()'), color='success', outline=True)
if __name__ == '__main__':
    start_server(main, port=80)