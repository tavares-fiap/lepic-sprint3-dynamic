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
    # print("\n=#=#=#=#=#=#=#=DEPURACAO INSERT USER=#=#=#=#=#=#=#=#=#=#=")
    # print(rankingTree)
    return

def searchUsersInRanking(rankingTree, score):
    if rankingTree == {}:
        return rankingTree
    if rankingTree['root'][0] > score:
        return searchUsersInRanking(rankingTree['left'], score)
    elif rankingTree['root'][0] < score:
        return searchUsersInRanking(rankingTree['right'], score)
    elif rankingTree['root'][0] == score:
        return rankingTree['root']
    return []

def deleteUserFromRanking(rankingTree, user):
    usersScoreList = searchUsersInRanking(rankingTree, user.highestScore)
    if len(usersScoreList) > 1:
        for i in range(1, len(usersScoreList)):  # Pular o primeiro elemento (que é o score)
            if usersScoreList[i].cpf == user.cpf:
                usersScoreList.pop(i)
                break
    # print("\n=#=#=#=#=#=#=#=DEPURACAO DELETE USER=#=#=#=#=#=#=#=#=#=#=")
    # print(rankingTree)