class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
    
    def make_deposit(self, amount):
        self.amount += amount
        return self
    
    def make_withdrawal(self, amount):
        self.amount -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

guido = User("Guido van Rossum")
monty = User("Monty Python")
amy = User("Amy Pissue")

guido.make_deposit(150).make_deposit(200).make_deposit(550).make_withdrawal(600).display_user_balance()

monty.make_deposit(50).make_deposit(400).make_withdrawal(100).make_withdrawal(25).display_user_balance()

amy.make_deposit(1000).make_withdrawal(75).make_withdrawal(100).display_user_balance()