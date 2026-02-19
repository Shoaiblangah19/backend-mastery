'''
### ⚡ Micro Task 2 (7 min)

Create a `Product` class with name, price, and category. Create a list of 5 products across 2-3 different categories and different prices.

Then write these operations (use list comprehensions where possible):
1. Find all products under a certain price
2. Find all products in a specific category
3. Find the most expensive product
4. Calculate total value of all products

Don't use a manager class yet — just work with the list directly.
'''

class Product:
    def __init__(self,name:str,price:float,category:str):
        self.name:str = name
        self.price:float = price
        self.category:str = category
    

products_list=[
    Product("Laptop",999,"Tech"),
    Product("PC",2000,"Tech"),
    Product("Protein",100,"Essentials"),
    Product("Chair",55,"Furniture"),
    Product("Fan",55,"Appliances")
]

tech_products=[item.name for item in products_list if item.category=="Tech"]
fifty_five = [item.name for item in products_list if item.price == 55]
expensive = max(item.price for item in products_list)
total = sum(item.price for item in products_list)

print(tech_products)
print(fifty_five)
print(expensive)
print(total)