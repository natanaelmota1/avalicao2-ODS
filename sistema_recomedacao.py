import csv
import random
import math
import json

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
    nearest = computeNearestneighbor (username, users)
    recommendations = []
    kVizinhos = []
    for i in range(5):
        neighborRatings = users[nearest[i][1]]
        kVizinhos.append(("#{} {}".format(i+1,nearest[i][1]),))
        userRatings = users[username]
        for filme in neighborRatings:
            if ((filme not in userRatings) and (filme not in recommendations)):
                if (neighborRatings[filme] >= 7):
                    recommendations.append((filme, neighborRatings[filme]))
        recommendations = sorted(recommendations,
                            key=lambda filmeTuple: filmeTuple[1],
                            reverse = True)
    kVizinhos.insert(0, ("Seus matchs de filmes",))
    recommendations.insert(0, ("Recomendações", "Notas"))
    return recommendations, kVizinhos

def MovieRec(username, movies, notas):
    with open('avaliacoes.json', 'r', encoding='utf-8') as json_file:
        users = json.load(json_file)

    avaliacao = {}
    if (users.get(username)):
        avaliacao = users[username]

    for i in range(len(movies)):    
        avaliacao[movies[i]] = notas[i]
        users[username] = avaliacao
    recomendacoes = recommend(username, users)
    with open('avaliacoes.json', 'w', encoding='utf-8') as file:
            json.dump(users, file, ensure_ascii=False, indent=4)
    return (recomendacoes[0], recomendacoes[1])

def geradorAvaliacoes():
    filmes = []
    usuarios = []

    with open('filmes.csv', mode='r', encoding='utf-8') as arq:
        leitor = csv.reader(arq, delimiter=',')
        for coluna in leitor:
            filmes.append(coluna[0])

    with open('usuarios.csv', mode='r', encoding='utf-8') as arq:
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
            avaliacao[filmes[i]] = random.randint(0, 10)
        users[usuario] = avaliacao
    
    with open('avaliacoes.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

# print(MovieRec("Evelyn da Rosa")[1])