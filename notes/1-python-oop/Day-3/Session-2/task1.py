'''
### ⚡ Micro Task 1 (5 min)

Create a `Product` class with `__init__(self, name: str, price: float, category: str)`.

Add a classmethod `from_dict(cls, data: dict)` that creates a Product from a dictionary like `{"name": "Laptop", "price": 999.99, "category": "Electronics"}`.

Create one product normally, one from a dict. Verify both have the same attributes accessible.
'''

class Product:
    def __init__(self,name:str,price:float,category:str):
        self.name:str =  name
        self.price:float = price
        self.category:str = category
    
    @classmethod
    def from_dict(cls,data:dict)->"Product":
        return cls(data["name"],data["price"],data["category"])
    

if __name__ == "__main__":

    # Test 1: Normal initialization
    try:
        p1 = Product("Laptop", 999.99, "Electronics")
        assert p1.name == "Laptop"
        assert p1.price == 999.99
        assert p1.category == "Electronics"
        print("Test 1 passed: Normal initialization works")
    except Exception as e:
        print(f"Test 1 failed: {e}")

    # Test 2: Create from dict using class method — WILL FAIL
    try:
        data = {"name": "Phone", "price": 599.99, "category": "Electronics"}
        p2 = Product.from_dict(data)
        assert p2.name == "Phone"
        assert p2.price == 599.99
        assert p2.category == "Electronics"
        print("Test 2 passed: from_dict works")
    except TypeError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 failed: {e}")

    # Test 3: Verify both products have same attribute types
    try:
        p1 = Product("Laptop", 999.99, "Electronics")
        data = {"name": "Phone", "price": 599.99, "category": "Electronics"}
        p2 = Product.from_dict(data)
        
        assert type(p1.name) == type(p2.name) == str
        assert type(p1.price) == type(p2.price) == float
        assert type(p1.category) == type(p2.category) == str
        print("Test 3 passed: Both products have same attribute types")
    except Exception as e:
        print(f"Test 3 failed: {e}")

    # Test 4: Verify from_dict returns Product instance
    try:
        data = {"name": "Tablet", "price": 399.99, "category": "Electronics"}
        p = Product.from_dict(data)
        assert isinstance(p, Product), f"Expected Product instance, got {type(p)}"
        print("Test 4 passed: from_dict returns Product instance")
    except Exception as e:
        print(f"Test 4 failed: {e}")

    # Test 5: Missing key in dict should raise KeyError
    try:
        data = {"name": "Incomplete", "price": 100.0}  # Missing 'category'
        p = Product.from_dict(data)
        print("Test 5 FAILED: Should have raised KeyError for missing key")
    except KeyError:
        print("Test 5 passed: Missing key raises KeyError")
    except TypeError:
        print("Test 5 skipped: from_dict not working due to missing decorator")
    except Exception as e:
        print(f"Test 5 failed: {e}")

    print("\nAll tests completed!")