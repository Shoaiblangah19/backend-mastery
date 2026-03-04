'''
### ⚡ Micro Task 1 (5 min)

Without running it, predict which lines crash and which work:

```python
class Contact:
    def __init__(self, name: str, email: str, phone: str | None = None):
        self.name = name
        self.email = email
        self.phone = phone

c = Contact("Ali", "ali@gmail.com")

print(c.name.upper())          # Line 1
print(c.phone.upper())         # Line 2
print(c.email.split("@")[1])   # Line 3
print(len(c.phone))            # Line 4
print(c.phone)                 # Line 5
```

Run it to verify your predictions. Understand WHY each one works or crashes.
'''

class Contact:
    def __init__(self, name: str, email: str, phone: str | None = None):
        self.name = name
        self.email = email
        self.phone = phone

c = Contact("Ali", "ali@gmail.com")

print(c.name.upper())          # Line 1 works
print(c.phone.upper())         # Line 2 won't work as phone is None
print(c.email.split("@")[1])   # Line 3 work
print(len(c.phone))            # Line 4 won't work as NoneType has no len
print(c.phone)                 # Line 5 Work and prints None