'''
### ⚡ Micro Task 2 (7 min)

Here's a badly organized class. Refactor it so ALL instance variables are in `__init__` with proper defaults. Methods should only MODIFY existing attributes, not create new ones:

'''
class ShoppingCart:
    def __init__(self, owner,coupon_code,discount):
        self.owner = owner
        self.coupon_code=coupon_code
        self.discount = discount
        self.items=[]
        self.total=0
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
        self.total += price
    
    def apply_coupon(self, code, discount):
        self.total = self.total * (1 - discount)