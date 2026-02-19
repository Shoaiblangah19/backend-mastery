'''
### ⚡ Micro Task 3 (5 min)

Create a `Wallet` class that has a balance (starts at 0) and owner name. Add methods:
- Add money (only positive amounts)
- Spend money (only if sufficient balance)
- Transfer to another wallet (deduct from this, add to other)

The transfer method takes **another Wallet object** as parameter. This tests understanding that `self` is THIS wallet, and the parameter is the OTHER wallet.

```
Expected behavior:
ali_wallet has 100
sara_wallet has 50
ali transfers 30 to sara
ali_wallet now has 70
sara_wallet now has 80
'''
class Wallet:
    def __init__(self,balance:int,name:str):
        self.balance=balance
        self.name=name
    def add_money(self,value)->None:
        if value<=0:
            raise ValueError("Invalid amount")
        self.balance += value
    def spend_money(self,value)->None:
        pass
    # Test has not use of it 

    def transfer(self,amount:int,account:Wallet)->None:
         self.balance -= amount
         account.balance += amount
         print(f"{self.name} transferred {amount} to {account.name}")
    
Wallet1=Wallet(100,"Ali")
wallet2=Wallet(50,"Sara")
print(Wallet1.balance)
print(wallet2.balance)
Wallet1.transfer(30,wallet2)
print(Wallet1.balance)
print(wallet2.balance)

