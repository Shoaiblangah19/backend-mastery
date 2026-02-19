'''
### ⚡ Micro Task 2 (7 min)

Create a `Book` class with `__init__` that takes: title, author, pages, and whether it's read or not.

Create 3 different book objects with different data. Print each book's title and author. Change one book's "read" status after creation and verify it changed.

Think about: what should the default be for "read" status? Should every book start as unread?
'''

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False

book1=Book("Islam and Daily Life","Haji Muhammad",300)
book2=Book("Exercises","Muhammad Shoaib",100)
book3=Book("Daily Habits","Muhammad Javaid",200)
print(f"Book 1: '{book1.title}' written by {book1.author}")
print(f"Book 2: '{book2.title}' written by {book2.author}")
print(f"Book 3: '{book3.title}' written by {book3.author}")
book1.read = True
print(book1.read)