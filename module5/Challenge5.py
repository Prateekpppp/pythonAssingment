class Account :

    def __init__(self, title, balance) :
        self.title = 0
        self.Balance = 0


class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title,balance)
        self.title = title
        self.balance = balance
        self.interestRate = interestRate

        print(title)
        print(balance)
        print(interestRate)


obj = SavingsAccount("Ashish", 5000, 5)

