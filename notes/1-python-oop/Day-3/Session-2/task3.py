'''
### ⚡ Micro Task 3 (7 min)

Create a `Book` class:
- `__init__(self, title: str, author: str, price: float)`
- `from_dict(cls, data: dict)` — create from dict
- `from_csv_row(cls, row: str)` — create from "title,author,price"
- `to_dict(self)` — convert to dict (reverse of from_dict)

Test the round-trip:
1. Create a book normally
2. Convert to dict with `to_dict()`
3. Create a NEW book from that dict with `from_dict()`
4. Verify both books have identical data

This round-trip test proves your serialization works correctly.
'''

class Book:
    def __init__(self,title:str,author:str,price:float):
        self.title:str = title
        self.author:str = author
        self.price:float = price
    
    @classmethod
    def from_dict(cls,data:dict)->"Book":
        return cls(data['title'],data['author'],data['price'])
    
    @classmethod
    def from_csv_row(cls,row:str)->"Book":
        parts=row.split(",")
        return cls(parts[0],parts[1],float(parts[2]))
    
    def to_dict(self)->dict:
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price
        }
    

if __name__ == "__main__":

    # Test 1: Normal initialization
    try:
        book = Book("Python Guide", "John Doe", 29.99)
        assert book.title == "Python Guide"
        assert book.author == "John Doe"
        assert book.price == 29.99
        print("Test 1 passed: Normal initialization works")
    except Exception as e:
        print(f"Test 1 failed: {e}")

    # Test 2: from_dict
    try:
        data = {"title": "Clean Code", "author": "Robert Martin", "price": 39.99}
        book = Book.from_dict(data)
        assert book.title == "Clean Code"
        assert book.author == "Robert Martin"
        assert book.price == 39.99
        print("Test 2 passed: from_dict works")
    except Exception as e:
        print(f"Test 2 failed: {e}")

    # Test 3: from_csv_row — WILL HAVE ISSUE
    try:
        book = Book.from_csv_row("The Pragmatic Programmer,Andy Hunt,49.99")
        assert book.title == "The Pragmatic Programmer"
        assert book.author == "Andy Hunt"
        assert book.price == 49.99, f"Expected 49.99 (float), got {book.price} ({type(book.price)})"
        print("Test 3 passed: from_csv_row works")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")
    except Exception as e:
        print(f"Test 3 failed: {e}")

    # Test 4: to_dict — WILL FAIL
    try:
        book = Book("Test Book", "Test Author", 19.99)
        result = book.to_dict()
        expected = {"title": "Test Book", "author": "Test Author", "price": 19.99}
        assert result == expected, f"Expected {expected}, got {result}"
        print("Test 4 passed: to_dict works")
    except TypeError as e:
        print(f"Test 4 FAILED: {e}")
    except Exception as e:
        print(f"Test 4 failed: {e}")

    # Test 5: Round-trip test — WILL FAIL due to to_dict issue
    try:
        # Step 1: Create book normally
        original = Book("Design Patterns", "Gang of Four", 54.99)
        
        # Step 2: Convert to dict
        book_dict = original.to_dict()
        
        # Step 3: Create new book from dict
        recreated = Book.from_dict(book_dict)
        
        # Step 4: Verify identical data
        assert original.title == recreated.title
        assert original.author == recreated.author
        assert original.price == recreated.price
        print("Test 5 passed: Round-trip works correctly")
    except Exception as e:
        print(f"Test 5 FAILED: {e}")

    # Test 6: Verify price type from csv is float
    try:
        book = Book.from_csv_row("Book,Author,25.50")
        assert isinstance(book.price, float), f"Price should be float, got {type(book.price)}"
        print("Test 6 passed: CSV price is float")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")
    except Exception as e:
        print(f"Test 6 failed: {e}")

    print("\nAll tests completed!")