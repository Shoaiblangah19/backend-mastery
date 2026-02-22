### ⚡ Micro Task 1 (5 min)
'''
Take this untyped class and add complete type hints — parameters, return values, and attribute hints where the type isn't obvious:
'''

class Product:
    def __init__(self, name:str, price:float, stock:int, tags:list[str] | None = None):
        self.name:str = name
        self.price:float = price
        self.stock:int = stock
        self.tags:list[str] = tags if tags is not None else []
        self.ratings:list[int] = []
        self.metadata:dict[str,str|int|bool] = {}
    
    def apply_discount(self, percent:float)->None:
        self.price = self.price * (1 - percent / 100)
    
    def add_rating(self, score:int)->None:
        self.ratings.append(score)
    
    def get_average_rating(self)->float:
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)
    
    def is_in_stock(self)->bool:
        return self.stock > 0
    
    def get_info(self)->dict[str, str|bool|float]:
        return {
            "name": self.name,
            "price": self.price,
            "in_stock": self.is_in_stock()
        }