'''
### ⚡ Micro Task 2 (7 min)

Create a `Student` class with:
- name (required, str)
- email (required, str)
- phone (optional, could be None)
- grades: list of floats
- courses: list of dicts (each dict has "name": str, "grade": float)
- mentor (optional, could be another Student or None)

Add these methods with proper return type hints:
- `get_average()` → float
- `get_course_names()` → list of strings
- `has_mentor()` → bool
- `set_mentor(mentor)` → None (parameter should be typed as Student)
- `get_top_course()` → dict or None (None if no courses)

Don't implement the logic — just write the signatures with type hints and `pass` in the body. The goal is practicing the HINTS, not the logic.
'''
class Student:
    def __init__(self,name:str,email:str,phone:str|None,grades:list[float],courses:list[dict[str,str|float]],mentor:'Student | None'=None):
        self.name:str = name
        self.email:str = email
        self.phone: str|None=phone
        self.grades:list[float]=grades
        self.courses:list[dict[str,str|float]]=courses
        self.mentor: Student|None=mentor
    def get_average(self)->float:
        pass
    def get_course_names(self)->list[str]:
        pass
    def has_mentor(self)->bool:
        pass
    def set_mentor(self,mentor:Student)->None:
        pass
    def get_top_course(self)->dict[str,str|float]:
        pass