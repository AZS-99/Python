class Account:
    def __init__(self, amount):
        self.balance = amount
        self.transaction_count = 0

    def deposit(self, amount):
        raise NotImplementedError

    def withdraw(self, amount):
        raise NotImplementedError


class Chequing(Account):
    def __init__(self, balance):
        super().__init__(balance)
        



if __name__ == '__main__':


