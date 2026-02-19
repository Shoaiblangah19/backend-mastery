'''
### ⚡ Micro Task 3 (8 min)

Create a `Task` class for a project management app using ALL 5 patterns:

- **Required:** At least 2 attributes that must be provided
- **Optional:** At least 2 attributes with sensible defaults
- **Auto-generated:** ID, creation timestamp, and a status field
- **Derived:** At least 1 attribute computed from other attributes
- **Collection:** At least 1 list attribute (mutable default handled correctly)

Include validation for at least 1 required field.

Create 2 task objects — one with only required fields, one with all fields. Print all attributes of both to verify:
- Auto-generated attributes are different for each object (different IDs)
- Collections are independent (add to one, other unaffected)
- Defaults work correctly
'''
import uuid
from datetime import datetime,timedelta

class Task:
    def __init__(self,title:str,due_date:int,description:str = "", is_completed:bool=False,tags=None):

        # Required
        if due_date<=1:
            raise ValueError("Invalid due date")
        self.title:str = title
        self.due_date:int = due_date

        # Optional
        self.description:str = description
        self.is_completed:bool = is_completed

        # Auto generated
        self.id:str=uuid.uuid4().hex[:8]
        self.created_at:str = datetime.now().isoformat()

        # Derived
        self.status = (datetime.now() + timedelta(days=self.due_date)).date()

        # Collections
        self.tags:list = tags if tags is not None else []



task1=Task("Create rest-api for client",3)
descrip="It is basically a gsoc contribution"
task2=Task("Make a pull request in the X orgs",7,descrip,False,["gsoc","contribution"])

print("Testing auto generated attributes for the Task 1")
print(task1.id)
print(task1.created_at)
print(task1.status)

print("Testing auto generated attributes for the Task 2")
print(task2.id)
print(task2.created_at)
print(task2.status)

print("Testing the Collection")
task1.tags.extend(["freelancing","earning"])
print(task1.tags)

task2.tags.extend(["contribution","gsoc"])
print(task2.tags)

