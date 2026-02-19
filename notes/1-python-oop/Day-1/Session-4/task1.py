'''
### ⚡ Micro Task 1 (5 min)

Create a `BankAccount` class with owner name and balance (starts at 0). Create 3 accounts. Deposit different amounts into each. Print all three balances to verify they're independent.

Then try this: assign `account_b = account_a` (not creating a new object, just copying the reference). Change `account_b.balance`. Check `account_a.balance`. What happened?
'''

class BackAccount:
    def __init__(self,owner:str,balance:float):
        self.owner:str = owner
        self.balance:float = balance
    

account1=BackAccount("Shoaib",1000)
account2=BackAccount("Muhammad Shoaib",500)
account3=BackAccount("Javaid",2000)

print(account1.balance)
print(account2.balance)
print(account3.balance)

account2 = account1

account2.balance = 700
print(account1.balance)