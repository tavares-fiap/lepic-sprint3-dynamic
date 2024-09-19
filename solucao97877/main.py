from user import User
from module import insert_user_in_ranking, update_user_high_score

user1 = User('Pedro', 'aaaa@gmail.com', 123)
user2 = User('Jao', 'aaaa@gmail.com', 456)
user3 = User('Jorge', 'aaaa@gmail.com', 789)
user4 = User('Alice', 'aaaa@gmail.com', 101112)
user5 = User('Beatriz', 'aaaa@gmail.com', 131415)
user6 = User('Joana', 'aaaa@gmail.com', 161718)

rankingTree = {
    'root' : [800],
    'left' : {},
    'right' : {}
}

print(f'\n=#=#=#=#=#=#=#=INICIAL TREE=#=#=#=#=#=#=#=#=#=#=')
print(rankingTree)

insert_user_in_ranking(rankingTree, user4)
insert_user_in_ranking(rankingTree, user5)
insert_user_in_ranking(rankingTree, user6)
insert_user_in_ranking(rankingTree, user3)
insert_user_in_ranking(rankingTree, user2)
insert_user_in_ranking(rankingTree, user1)

print(f'\n=#=#=#=#=#=#=#=USERS INSERTED=#=#=#=#=#=#=#=#=#=#=')
print(rankingTree)

update_user_high_score(rankingTree,user1,800)
update_user_high_score(rankingTree,user2,350)
update_user_high_score(rankingTree,user3,350)
update_user_high_score(rankingTree,user4,120)
update_user_high_score(rankingTree,user5,1800)
update_user_high_score(rankingTree,user6,100)

print(f'\n=#=#=#=#=#=#=#=USERS SCORE UPDATED=#=#=#=#=#=#=#=#=#=#=')
print(rankingTree)
