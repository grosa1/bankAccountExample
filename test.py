from BankAccount import BankAccount
from CustomerAccount import CustomerAccount

account = BankAccount("Giovanni", "1", 1000)
account.accountInfo()
account.deposit(500)
account.withdraw(1200)
account.accountInfo()

account = BankAccount("Marco", "2", 500)
account.accountInfo()
account.deposit(1400)
account.withdraw(2000)
account.withdraw(200)
account.accountInfo()