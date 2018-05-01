from BankAccount import BankAccount
from AccountManager import AccountManager


account1 = BankAccount("Giovanni", "1", 1000)
account1.accountInfo()

account2 = BankAccount("Marco", "2", 500)
account2.accountInfo()

res = AccountManager.bankTransfer(account1, account2, 100)
print(str(res))

account1.accountInfo()
account2.accountInfo()


