class User():
    def __init__ (self, name, email, cpf):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.highestScore = 0

    def newHighScore(self, highScore):
        self.highestScore = highScore