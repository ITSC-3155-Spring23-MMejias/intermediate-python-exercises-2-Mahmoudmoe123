from BankAccount import BankAccount

account = BankAccount("Mahmoud Mohamed", 6000)
account.deposit(389.25)
account.withdraw(50)
print(account.get_balance())