'''
### ⚡ Micro Task 3 (~10 min)

```
Create a class `TaskManager`:
  - __init__() starts with empty task list

  Chainable methods (return self):
  - add(title: str, priority: int) → adds task dict to list
  - remove(title: str) → removes task by title (if exists)
  - sort_by_priority() → sorts tasks by priority (1 = highest)


Test with chaining:
  result = (
      TaskManager()
      .add("Deploy API", 1)
      .add("Write tests", 2)
      .add("Fix typo", 3)
      .remove("Fix typo")
      .sort_by_priority()
      .display()
  )
  print(result)
  
Expected output:
  [1] Deploy API
  [2] Write tests

Also test: what happens if you call .remove("nonexistent")?
It should NOT crash — just do nothing and keep the chain alive.

Time: 10 minutes.
'''

class TaskManager:
    def __init__(self):
        self.tasks:list[dict]=[]
    def add(self,title:str,priority:int)->None:
        self.tasks.append({
            "title":title,
            "priority":priority
        })
        return self
    def remove_task(self,title:str)->"TaskManager":
         self.tasks=[task for task in self.tasks if task["title"]!=title]
         return self
    def sort_by_priority(self)->"TaskManager":
        self.tasks.sort(key=lambda x: x["priority"])
        return self
    
result = (
      TaskManager()
      .add("Deploy API", 1)
      .add("Write tests", 2)
      .add("Fix typo", 3)
      .remove_task("Fix typo")
      .remove_task("Fix typo")
      .sort_by_priority()
  )
print(result.__dict__)