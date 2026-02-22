'''
### ⚡ Micro Task 2 (~7 min)

```
Create a class `GradeBook`:
  - __init__ takes subject (str)
  - stores grades internally as list of dicts:
      {"student": str, "score": float}

  - add_grade(student: str, score: float) → returns dict:
      If score < 0 or > 100: return {"success": False, "error": "..."}
      Otherwise add and return {"success": True, "student": name, "score": score}

  - average() → float (average of all scores)
      If no grades: return 0.0

  - highest() → dict or None
      Returns the full grade dict of highest scorer
      If no grades: return None

Test:
  gb = GradeBook("Math")
  print(gb.add_grade("Alice", 92))    → {"success": True, ...}
  print(gb.add_grade("Bob", 105))     → {"success": False, "error": "..."}
  gb.add_grade("Charlie", 88)
  print(gb.average())                 → 90.0
  print(gb.highest())                 → {"student": "Alice", "score": 92}

Time: 7 minutes.
'''

class GradeBook:
    def __init__(self,subject:str):
        self.subject:str = subject
        self.total:int = 0
        self.grades:list[dict]=[]
    
    def add_grade(self,student:str,score:float)->dict:
        if score<0 or score>100:
            return {
                "success":False,
                "error":"invalid score"
            }
        self.grades.append({
            "student":student,
            "score":score
        })
        self.total += score
        return {
            "success":True,
            "student":student,
            "score":score
        }
    
    def average(self)->float:
        return self.total/len(self.grades)
    
    def get_heighest(self):
        if len(self.grades)==0:
            return None
        result={
            "student":"",
            "score":0
        }   
        for grade in self.grades:
            if grade["score"]>=result["score"]:
                result["score"]=grade["score"]
                result["student"]=grade["student"]
        return result


gb = GradeBook("Math")
print(gb.add_grade("Alice", 92))    #→ {"success": True, ...}
print(gb.add_grade("Bob", 105))     #→ {"success": False, "error": "..."}
gb.add_grade("Charlie", 88)
print(gb.average())                 #→ 90.0
print(gb.get_heighest())  