'''
### ⚡ Micro Task 1 (5 min)

Create a `Contact` class with two static methods:
- `is_valid_phone(phone: str) -> bool` — returns True if phone starts with "03" or "+92" and has at least 10 digits
- `format_phone(phone: str) -> str` — removes spaces and dashes, returns clean number

Use both inside `__init__` to validate and clean the phone number.

Test: `Contact("Ali", "ali@gmail.com", "0300-123 4567")` should store phone as `"03001234567"`. Invalid phone should raise ValueError.
'''

class Contact:
    def __init__(self,name:str,email:str,phone:str):
        self.name:str = name
        self.email:str = email
        phoneNow=self.format_phone(phone)
        if self.is_valid_phone(phoneNow):
            self.phone:str = phoneNow
        
    @staticmethod
    def is_valid_phone(phone:str)->bool:
        if len(phone)<11:
            raise ValueError("Invalid length of phone")
        if not  phone.startswith(("03","+92")):
            raise ValueError("invalid phone number")
        return True
    
    @staticmethod
    def format_phone(phone:str)->str:
        return phone.replace(" ","").replace("-","")
    

try:
    contact = Contact("Ali","ali@gmail.com","0300-123 4589")
    print(contact.__dict__)
except Exception as e:
    print(e)
