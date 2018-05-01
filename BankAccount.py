from CustomerAccount import CustomerAccount

class BankAccount(CustomerAccount):

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
            print("AMOUNT ERROR\n")
        else:
            self.__balance -= amount
            print(str(amount) + " WITHDRAW. NEW BALANCE: " + str(self.__balance) + "\n")
        
    def deposit(self, amount):
        if amount < 0:
            print("AMOUNT ERROR\n")
        else:
            self.__balance += amount
            print(str(amount) + " DEPOSIT. NEW BALANCE: " + str(self.__balance) + "\n")
        
    def accountInfo(self):
        print("OWNER: " + super().owner + "\n" + "ACCOUNT: " + super().accountNumber + "\n" + "BALANCE: " + str(self.__balance) + "\n")


