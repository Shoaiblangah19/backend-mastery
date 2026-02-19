'''
### ⚡ Micro Task 2 (7 min)

Create a `Counter` class that:
- Starts at 0 when created
- Has a method to increment by 1
- Has a method to increment by a custom amount
- Has a method to reset to 0
- Has a method that returns a string like `"Counter: 5"`

The increment-by-custom-amount method should call the increment-by-1 method internally (use `self.method()` to call another method).

Create a counter, increment it 3 times by 1, then once by 10, print the value, then reset and print again.

Expected behavior: Counter goes to 13, then back to 0.
'''

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self)->None:
        self.count += 1
    def custome_increment(self,value)->None:
        for _ in range(value):
            self.increment()
    def reset(self)->None:
        self.count = 0
    def show(self)->str:
        return f"Counter: {self.count}"

counter=Counter()
counter.increment()
counter.increment()
counter.increment()
counter.custome_increment(10)
print(counter.count)
counter.reset()
print(counter.count)