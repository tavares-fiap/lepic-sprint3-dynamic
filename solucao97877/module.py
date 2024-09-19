from typing import Union, Dict, List
from user import User

def search_specific_node(ranking_tree : dict, score : int) -> Union[Dict, List]:
    if ranking_tree == {}:
        return ranking_tree
    if ranking_tree['root'][0] > score:
        return search_specific_node(ranking_tree['left'], score)
    elif ranking_tree['root'][0] < score:
        return search_specific_node(ranking_tree['right'], score)
    else:
        return ranking_tree['root']
    
def insert_user_in_ranking(ranking_tree : dict, user : User):
    users_with_same_score = search_specific_node(ranking_tree, user.highest_score)
    # Verificação se 'search_specific_node' devolveu uma lista
    if isinstance(users_with_same_score, list):
        for existing_user in users_with_same_score[1:]:
            if existing_user.cpf == user.cpf:
                print(f"Usuário {user.cpf} já está nessa posicao do ranking!")
                return
        users_with_same_score.append(user)  # Adiciona o usuário à lista
    else:
        # Novo score, cria um novo nó na árvore
        users_with_same_score['root'] = [user.highest_score, user]
        users_with_same_score['left'] = {}
        users_with_same_score['right'] = {}
    return

def delete_user_from_ranking(ranking_tree : dict, user : User):
    users_with_same_score = search_specific_node(ranking_tree, user.highest_score)
    if isinstance(users_with_same_score, list) and len(users_with_same_score) > 1:
        for i in range(1, len(users_with_same_score)):  # Pular o primeiro elemento (que é o score)
            if users_with_same_score[i].cpf == user.cpf:
                users_with_same_score.pop(i)
                break
    return

def update_user_high_score(rankingTree : dict, user : User, highScore : int):
    delete_user_from_ranking(rankingTree, user) # Deleta buscando usuario com o score antigo
    user.new_high_score(highScore) # Altera para score novo
    insert_user_in_ranking(rankingTree, user) # Insere com score novo
    return