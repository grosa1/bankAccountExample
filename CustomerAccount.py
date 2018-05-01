class CustomerAccount:

    def __init__(self, owner, accountNumber):
        self.__owner = owner
        self.__accountNumber = accountNumber

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, newOwner):
        self.__owner = newOwner

    @property
    def accountNumber(self):
        return self.__accountNumber

    @accountNumber.setter
    def accountNumber(self, newAccountNumber):
        self.__accountNumber = newAccountNumber