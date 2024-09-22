def inserir(ranking, score, nome, cpf):
    if str(score) in ranking.keys():
        ranking[str(score)].append({"nome": nome, "cpf": cpf})
    else:
        ranking[str(score)] = [{"nome": nome, "cpf": cpf}]
    novo_ranking = ordenar_dicionario_merge_sort(ranking)
    return novo_ranking


def excluir(ranking, cpf):
    for key, value in ranking.items():
        for usuario in value:
            if usuario['cpf'] == cpf:
                score = key
    # Verifica se o score (convertido para string) existe no ranking
    if str(score) in ranking:
        # Itera sobre a lista de usuários no score especificado
        for usuario in ranking[str(score)]:
            # Verifica se o CPF corresponde
            if usuario['cpf'] == cpf:
                nome = usuario['nome']
                # Remove o usuário da lista
                ranking[str(score)].remove(usuario)
                # Se a lista ficar vazia após a remoção, remove o score também
                if not ranking[str(score)]:
                    del ranking[str(score)]
                return nome  # Indica que o usuário foi removido
    return False  # Indica que o usuário não foi encontrado

def atualizar_score (ranking, novo_score, cpf):
    nome = excluir(ranking, cpf)
    if nome != False:
        novo_ranking = inserir(ranking, novo_score, nome, cpf)
        return novo_ranking
    return print("ERRO! Não foi possível atualizar, Usuário Inexistente!")


# Função para mesclar duas sublistas de pares
def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Comparar e mesclar os pares
    while i < len(esquerda) and j < len(direita):
        if int(esquerda[i][0]) > int(direita[j][0]):  # Ordenação decrescente
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adicionar os elementos restantes
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

# Função para implementar o Merge Sort
def merge_sort(pares):
    if len(pares) <= 1:
        return pares
    
    # Dividir a lista no meio
    meio = len(pares) // 2
    esquerda = merge_sort(pares[:meio])
    direita = merge_sort(pares[meio:])
    
    # Mesclar as duas metades
    return merge(esquerda, direita)

# Função para ordenar o dicionário usando Merge Sort
def ordenar_dicionario_merge_sort(dicionario):
    # Converter o dicionário em uma lista de pares (chave, valor)
    pares = list(dicionario.items())
    
    # Ordenar os pares usando Merge Sort
    pares_ordenados = merge_sort(pares)
    
    # Reconstruir o dicionário ordenado
    dicionario_ordenado = dict(pares_ordenados)
    
    return dicionario_ordenado

ranking = {
    "800": [{"nome": "Nikolas", "cpf": 111}],
    "500": [{"nome": "Pedro", "cpf": 222}, {"nome": "Rodrigo", "cpf": 333}],
    "300": [{"nome": "Thiago", "cpf": 444}]
}

print("#"*150)
print(">"*67+"RANKING INICIAL"+"<"*67)
print("#"*150)
print(ranking)
print("#"*150)
print(">"*59+"ADICIONANDO CPF 555 SCORE: 1800"+"<"*59)
print("#"*150)
print(inserir(ranking, 1800, "Guilherme", 555))
print("#"*150)
print(">"*59+"ADICIONANDO CPF 666 SCORE: 300"+"<"*59)
print("#"*150)
print(inserir(ranking, 300, "João", 666))
print("#"*150)
print(">"*59+"ATUALIZANDO SCORE DO CPF 111 PARA 2000"+"<"*59)
print("#"*150)
print(atualizar_score(ranking, 2000, 111))
print("#"*150)
print(">"*59+"ATUALIZANDO SCORE DO CPF 444 PARA 1300"+"<"*59)
print("#"*150)
print(atualizar_score(ranking, 1300, 444))