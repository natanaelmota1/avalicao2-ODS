import csv
import random
import math
import numpy as np

def euclidiana(rating1, rating2):
    distance = 0
    for key in rating1:
        if (key in rating2):
            distance += math.pow(rating1[key] - rating2[key], 2)
    return round(math.sqrt(distance), 1)

def computeNearestneighbor (username, users):
    distances = []
    for user in users:
        if user != username:
            distance = euclidiana(users[username], users[user])
            distances.append((distance, user))
    distances.sort()
    return distances

def recommend(username, users): 
    #first find nearest neighbor
    nearest = computeNearestneighbor (username, users) [0][1]
    recommendations = []
    #now find bands neighbor rated that user didn't 
    neighborRatings = users[nearest]
    userRatings = users[username]
    for filme in neighborRatings:
        if not filme in userRatings:
            if (neighborRatings[filme] >= 4):
                recommendations.append((filme, neighborRatings[filme]))
    #using the fn sorted for variety - sort is more efficient
    return sorted(recommendations,
                          key=lambda filmeTuple: filmeTuple[1],
                          reverse = True)
def MovieRec(username):
    filmes = []
    usuarios = []

    with open('filmes.csv', mode='r') as arq:
        leitor = csv.reader(arq, delimiter=',')
        for coluna in leitor:
            filmes.append(coluna[0])

    with open('usuarios.csv', mode='r') as arq:
        leitor = csv.reader(arq, delimiter=',')
        for coluna in leitor:
            usuarios.append(coluna[0])

    users = {}
    for usuario in usuarios:
        posicoes = []
        avaliacao = {}
        while (len(posicoes) < 20):
            posicao = random.randint(0, 99)
            if (posicao not in posicoes):
                posicoes.append(posicao)
        for i in posicoes:        
            avaliacao[filmes[i]] = round(random.uniform(1, 5), 1)
        users[usuario] = avaliacao

    return (recommend(username, users))
    np.savetxt("recomendacoes.csv", recommend(username, users), delimiter =",",fmt ='% s')