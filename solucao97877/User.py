from module import deleteUserFromRanking, insertUserInRanking

class User():
    def __init__ (self, name, email, cpf):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.highestScore = 0

    def newHighScore(self, highScore, rankingTree):
        deleteUserFromRanking(rankingTree, self) # Deleta buscando usuario com o score antigo
        self.highestScore = highScore # Altera para score novo
        insertUserInRanking(rankingTree, self) # Insere com score novo
    
    def __repr__(self):
        return f"User(name='{self.name}', cpf='{self.cpf}')"