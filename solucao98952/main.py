lista_jogadores = [['Rodrigo', 800], ['Nikolas', 500], ['Pedro', 200]]
lista_score_organizada = []

def organizaScore(lista_jogadores):
    while lista_jogadores:
        maior_valor = lista_jogadores[0][1]  
        indice_maior = 0
        
        for i in range(1, len(lista_jogadores)):
            if lista_jogadores[i][1] > maior_valor:  
                maior_valor = lista_jogadores[i][1]
                indice_maior = i

        lista_score_organizada.append(lista_jogadores.pop(indice_maior))
    return lista_score_organizada
    

def novoScore(lista_jogadores):
    nome =  'Rodrigo' # tente um nome já existente, por exemplo: 'Rodrigo'
    score = 237
    if verJogador(nome,score,lista_jogadores) == True:
        organizaScore(lista_jogadores)
    else:
        lista_jogadores.append((nome, score))
        organizaScore(lista_jogadores)

    for i, (nome, score) in enumerate(lista_score_organizada, start=1):
        print(f"{i}: {nome} - pontuação: {score}")


def verJogador(nome,score,lista_jogadores):
    for i in range(len(lista_jogadores)):
        if nome == lista_jogadores[i][0]:
            lista_jogadores[i][1] = score
            return True
    return False

novoScore(lista_jogadores)






