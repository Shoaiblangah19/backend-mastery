'''
### ⚡ Micro Task 1 (5 min)

Look at this code and identify which variables are instance variables and which are local variables. Then predict what `print(p.x)` will output for each case — will it work or crash?
'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        discount = 0.1
        self.tags = []
    
    def apply_discount(self, percent):
        savings = self.price * (percent / 100)
        self.price = self.price - savings
        return savings

p = Product("Laptop", 1000)

# Which of these work? Which crash?
print(p.name)  #Laptop
print(p.price)  # 1000
# print(p.discount) # Error no attribute
print(p.tags)    # []
print(p.savings)  # Error no attribute