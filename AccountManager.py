from BankAccount import BankAccount
class AccountManager:
    @staticmethod
    def bankTransfer(sourceAccount, targetAccount, amount):
        operation = sourceAccount.withdraw(amount)
        if operation:
            operation = targetAccount.deposit(amount)
            return True
        
        return False