from CustomerAccount import CustomerAccount
class BankAccount(CustomerAccount):
    
    __balance = 0

    def __init__(self, owner, accountNumber, balance):
        super().__init__(owner, accountNumber)
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, newBalance):
        self.__balance = newBalance

    def withdraw(self, amount):
        if amount > self.__balance or amount < 0:
            return False
        else:
            self.__balance -= amount
            return True
        
    def deposit(self, amount):
        if amount < 0:
            return False
        else:
            self.__balance += amount
            return True
        
    def accountInfo(self):
        print("OWNER: " + super().owner + "\n" + "ACCOUNT: " + super().accountNumber + "\n" + "BALANCE: " + str(self.__balance) + "\n")


