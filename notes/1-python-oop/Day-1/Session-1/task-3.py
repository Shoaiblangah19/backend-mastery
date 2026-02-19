'''
### ⚡ Micro Task 3 (8 min)

Create a `Task` class for a todo app. It should have:
- Some required attributes (think about what's essential for a task)
- Some optional attributes with sensible defaults
- At least one auto-set attribute (not passed in by user)
- A list-type attribute (use the mutable default pattern correctly!)

Create 3 tasks — one with only required fields, one with some optional fields, one with all fields. Print all attributes of each task to verify everything works. Add an item to one task's list attribute and verify other tasks aren't affected.
'''
from datetime import datetime
class Task:
    def __init__(self,title:str,isCompleted:bool=False,tags=None):
        # Required
        self.title=title

        # Optional
        self.is_completed:bool = isCompleted

        # auto set attribute
        self.created_at:str = datetime.now().isoformat()

        # list type attribute
        self.tags:list = tags if tags is not None else []

task1=Task("Daily complete one day of backend mastery")
task2=Task("DSA and CP",False)
task3=Task("Exercises",False,["cardio","leg","chest"])

print(f"Task 1 testing all attributes: {'*' * 60}")
print(task1.title)
print(task1.is_completed)
print(task1.created_at)
print(task1.tags)

print(f"Task 2 testing all attributes: {'*' * 60}")
print(task2.title)
print(task2.is_completed)
print(task2.created_at)
print(task2.tags)

print(f"Task 3 testing all attributes: {'*' * 60}")
print(task3.title)
print(task3.is_completed)
print(task3.created_at)
print(task3.tags)


task3.tags.append("Back")
print(task3.tags)