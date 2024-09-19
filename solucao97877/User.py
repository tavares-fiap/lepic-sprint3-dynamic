

class User():
    def __init__ (self, name, email, cpf):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.highest_score = 0

    def new_high_score(self, highScore):
        self.highest_score = highScore
    
    def __repr__(self):
        return f"User(name='{self.name}', cpf='{self.cpf}')"