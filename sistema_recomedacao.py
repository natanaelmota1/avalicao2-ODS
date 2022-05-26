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

    with open('conteudos.json', 'r', encoding='utf-8') as json_file:
        usersConteudo = json.load(json_file)    

    with open('filmes.json', 'r', encoding='utf-8') as json_file:
        filmesDic = json.load(json_file)

    avaliacao = {}
    if (users.get(username)):
        avaliacao = users[username]
    
    usersConteudo[username] = vinculaConteudo(username, users, filmesDic)

    for i in range(len(movies)):    
        avaliacao[movies[i]] = notas[i]
        users[username] = avaliacao

    
    recomendacoes = recommend(username, users)
    with open('avaliacoes.json', 'w', encoding='utf-8') as file:
        json.dump(users, file, ensure_ascii=False, indent=4)

    with open('conteudos.json', 'w', encoding='utf-8') as file:
        json.dump(usersConteudo, file, ensure_ascii=False, indent=4)

    return (recomendacoes[0], recomendacoes[1])

def geradorAvaliacoes():
    usuarios = []
    filmes = []
    filmesDic = {}

    with open('filmes.csv', mode='r', encoding='utf-8') as arq:
        leitor = csv.reader(arq, delimiter=',')
        for coluna in leitor:
            filmes.append(coluna[0])
            conteudo = {}
            conteudo["diretor"] = coluna[1]
            conteudo["ano"] = coluna[2]
            conteudo["pais"] = coluna[3]
            conteudo["genero"] = coluna[4]
            filmesDic[coluna[0]] = conteudo
    
    with open('filmes.json', 'w', encoding='utf-8') as file:
        json.dump(filmesDic, file, ensure_ascii=False, indent=4)


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
    
    usersConteudo = {}

    for usuario in usuarios:
        usersConteudo[usuario] = vinculaConteudo(usuario, users, filmesDic)
        
    
    with open('conteudos.json', 'w', encoding='utf-8') as file:
        json.dump(usersConteudo, file, ensure_ascii=False, indent=4)

def contaConteudo(busca, conteudo, conteudos, filmes):
    count = 0
    for key in filmes:
        filme = conteudos[key]
        if (filme[conteudo] == busca):
            count+=1
    return count

def vinculaConteudo(usuario, users, filmesDic):
    conteudo = {}
    diretor = {}
    ano = {}
    pais = {}
    genero = {}
    for filme in users[usuario]:
        filmeDic = filmesDic[filme]
        verifica = diretor.get(filmeDic["diretor"], "null")
        if (verifica == "null"):
            diretor[filmeDic["diretor"]] = contaConteudo(filmeDic["diretor"],"diretor", filmesDic, users[usuario])
        
        verifica = ano.get(filmeDic["ano"], "null")
        if (verifica == "null"):
            ano[filmeDic["ano"]] = contaConteudo(filmeDic["ano"],"ano", filmesDic, users[usuario])
        
        verifica = pais.get(filmeDic["pais"], "null")
        if (verifica == "null"):
            pais[filmeDic["pais"]] = contaConteudo(filmeDic["pais"],"pais", filmesDic, users[usuario])
        
        verifica = genero.get(filmeDic["genero"], "null")
        if (verifica == "null"):
            genero[filmeDic["genero"]] = contaConteudo(filmeDic["genero"],"genero", filmesDic, users[usuario])
    conteudo["diretor"] = diretor
    conteudo["ano"] = ano
    conteudo["pais"] = pais
    conteudo["genero"] = genero
    return conteudo

# print(MovieRec("Evelyn da Rosa")[1])
geradorAvaliacoes()