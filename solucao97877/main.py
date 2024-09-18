from user import User

def insertUserInRanking(rankingTree, user):
    while rankingTree != {}:
        if rankingTree['root'][0] > user.highestScore:
            rankingTree = rankingTree['left']
        elif rankingTree['root'][0] < user.highestScore:
            rankingTree = rankingTree['right']
        else:
            for i in range(1, len(rankingTree['root'])): # Verifica se usuario ja esta entre os usuarios com aquele mesmo score
                if rankingTree['root'][i].cpf == user.cpf:
                    print(f"Usuario {user.cpf} ja esta no ranking!")
                    return
            rankingTree['root'].append(user) # Se nao estiver, adiciona usuario aquela posicao
            return
    rankingTree['root'] = [user.highestScore, user] # Se for Score completamente novo, cria nova ramificacao da arvore
    rankingTree['left'] = {}
    rankingTree['right'] = {}
    return

def searchUsersInRanking(rankingTree, score):
    if rankingTree == {}:
        return rankingTree
    if rankingTree['root'][0] > score:
        return searchUsersInRanking(rankingTree['left'], score)
    elif rankingTree['root'][0] < score:
        return searchUsersInRanking(rankingTree['right'], score)
    elif rankingTree['root'][0] == score:
        # Retorna apenas usuarios
        return rankingTree['root']
    return []

def deleteUserFromRanking(rankingTree, user):
    usersScoreList = searchUsersInRanking(rankingTree, user.highestScore)
    if len(usersScoreList) > 1:
        for i in range(1, len(usersScoreList)):  # Pular o primeiro elemento (que é o score)
            if usersScoreList[i].cpf == user.cpf:
                usersScoreList.pop(i)
                break

def updateUserRanking(rankingTree, user):
    deleteUserFromRanking(rankingTree, user)
    insertUserInRanking(rankingTree, user)

rankingTree = {}

user1 = User('Pedro', 'aaaa@gmail.com', 123)
user2 = User('Jao', 'aaaa@gmail.com', 456)
user3 = User('Jorge', 'aaaa@gmail.com', 789)
user4 = User('Alice', 'aaaa@gmail.com', 101112)

print(rankingTree)

insertUserInRanking(rankingTree, user4)
insertUserInRanking(rankingTree, user3)
insertUserInRanking(rankingTree, user2)
insertUserInRanking(rankingTree, user1)

print(rankingTree)

user1.newHighScore(600)
user2.newHighScore(350)
user3.newHighScore(350)
user4.newHighScore(800)
updateUserRanking(rankingTree, user1)
updateUserRanking(rankingTree, user2)
updateUserRanking(rankingTree, user3)
updateUserRanking(rankingTree, user4)

print(rankingTree)
