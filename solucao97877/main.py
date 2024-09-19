from user import User
from module import insertUserInRanking

user1 = User('Pedro', 'aaaa@gmail.com', 123)
user2 = User('Jao', 'aaaa@gmail.com', 456)
user3 = User('Jorge', 'aaaa@gmail.com', 789)
user4 = User('Alice', 'aaaa@gmail.com', 101112)
user5 = User('Beatriz', 'aaaa@gmail.com', 131415)
user6 = User('Joana', 'aaaa@gmail.com', 161718)

rankingTree = {
    'root' : [800, user1],
    'left' : {
        'root' : [350, user2, user3],
        'left' : {},
        'right' : {}
    },
    'right' : {}
}

print(f'\n=#=#=#=#=#=#=#=INICIAL TREE=#=#=#=#=#=#=#=#=#=#=')
print(rankingTree)

insertUserInRanking(rankingTree, user4)
insertUserInRanking(rankingTree, user5)
insertUserInRanking(rankingTree, user6)
insertUserInRanking(rankingTree, user3)
insertUserInRanking(rankingTree, user2)
insertUserInRanking(rankingTree, user1)

print(f'\n=#=#=#=#=#=#=#=USERS INSERTED=#=#=#=#=#=#=#=#=#=#=')
print(rankingTree)

user1.newHighScore(800, rankingTree)
user2.newHighScore(350, rankingTree)
user3.newHighScore(350, rankingTree)
user4.newHighScore(120, rankingTree)
user5.newHighScore(1800, rankingTree)
user6.newHighScore(100, rankingTree)

print(f'\n=#=#=#=#=#=#=#=USERS SCORE UPDATED=#=#=#=#=#=#=#=#=#=#=')
print(rankingTree)
