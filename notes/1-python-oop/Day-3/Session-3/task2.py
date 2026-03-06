'''
### ⚡ Micro Task 2 (5 min)

Create a `Password` class with `__init__(self, raw_password: str)` that validates the password using static methods.

Static methods needed:
- `has_minimum_length(password: str, min_len: int = 8) -> bool`
- `has_digit(password: str) -> bool`
- `has_uppercase(password: str) -> bool`

`__init__` should call all three and raise `ValueError` with a specific message for whichever check fails.

Test with: `"short"`, `"alllowercase123"`, `"NoDigitsHere"`, `"ValidPass123"`.
'''

class Password:
    def __init__(self,raw_password:str):
        if self.has_minimum_length(raw_password) and self.has_digit(raw_password) and self.has_upper(raw_password):
         self.raw_password:str = raw_password
        else:
            raise ValueError('invalid password')

    @staticmethod
    def has_minimum_length(password:str,min_len:int=8)->bool:

        if not len(password)>=min_len:
            raise ValueError("invalid length")
        return True
    @staticmethod
    def has_digit(password:str)->bool:
        if not any(char.isdigit() for char in password):
            raise ValueError("has no digit")
        return True
    @staticmethod
    def has_upper(password:str)->bool:
        if not any(char.isupper() for char in password):
            raise ValueError("has no uppercase letter")
        return True
    
# password = Password("short")
# password = Password("alllowercase123")
# password = Password("NoDigitsHere")
password = Password("ValidPass123")
print(password.raw_password)