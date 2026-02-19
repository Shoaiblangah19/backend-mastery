'''
### ⚡ Micro Task 1 (5 min)

Create a `Book` class with title and author in `__init__`. Add a method `describe()` that returns `"[title] by [author]"`.

Create 2 book objects. Call `describe()` on both normally. Then call it using the `Contact.greet(ali)` syntax (i.e., `Book.describe(your_book_object)`) to prove `self` is just the object being passed.

Both calls should give same output.
'''

class Book:
    def __init__(self,title:str,author:str):
        self.title:str=title
        self.author:str=author

    def describe(self)->str:
        return f"[{self.title}] by [{self.author}]"

book1=Book("Exercises","Muhammad Shoaib")
book2=Book("Coding","Muhammad Javaid")

print(book1.describe())
print(book2.describe())

print(Book.describe(book1))