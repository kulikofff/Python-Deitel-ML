from account import Account
from decimal import Decimal

account1 = Account('John Green', Decimal('50.00'))
print(account1.name, account1.balance)

account1.deposit(Decimal('25.53'))
print(account1.name, account1.balance)


