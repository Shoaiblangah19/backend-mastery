'''
### ⚡ Micro Task 3 (5 min)

Given this data, write code that safely extracts all cities from contacts that HAVE an address, without any crashes:

```python
contacts = [
    {"name": "Ali", "address": {"city": "Lahore", "country": "PK"}},
    {"name": "Sara", "address": None},
    {"name": "Hassan"},  # no address key at all
    {"name": "Fatima", "address": {"country": "PK"}},  # no city key
    {"name": "Omar", "address": {"city": "Karachi", "country": "PK"}},
]

# Expected output: ["Lahore", "Karachi"]
# Must not crash on any contact
```

Use `.get()` for safe dict access and `is not None` checks. Write it as a list comprehension or a loop — your choice.
'''
contacts = [
    {"name": "Ali", "address": {"city": "Lahore", "country": "PK"}},
    {"name": "Sara", "address": None},
    {"name": "Hassan"},  # no address key at all
    {"name": "Fatima", "address": {"country": "PK"}},  # no city key
    {"name": "Omar", "address": {"city": "Karachi", "country": "PK"}},
]

# cities=[]
# for value in contacts:
#  if value.get("address") is not None:
#    if value.get("address").get("city") is not None:
#      cities.append(value.get("address").get('city'))

# OR

cities=[
    value.get("address").get("city")
    for value in contacts
    if value.get('address') is not None and value.get('address').get('city') is not None
]

print(cities)