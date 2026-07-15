class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance
        self.number_of_accounts = len(balance)
        
    def is_valid_account(self, account: int):
        return 1 <= account <= self.number_of_accounts

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid_account(account1):
            return False
        if not self.is_valid_account(account2):
            return False
        index1 = account1 - 1
        index2 = account2 - 1
        if self.balance[index1] < money:
            return False
        self.balance[index1] -= money
        self.balance[index2] += money
        return True
        

    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            return False
        index = account - 1
        self.balance[index] += money
        return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            return False
        index = account - 1
        if self.balance[index] < money:
            return False
        self.balance[index] -= money
        return True
        

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)