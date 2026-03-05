'''
### ⚡ Micro Task 2 (7 min)

Create a `Task` class with `__init__(self, title: str, priority: str = "medium", due_date: str | None = None)`.

Add these classmethods:
- `from_dict(cls, data: dict)` — creates from dict
- `from_csv_row(cls, row: str)` — creates from "title,priority,due_date" string
- `create_urgent(cls, title: str)` — creates with priority="critical" and due_date="today"

Test all three. Also verify that `from_csv_row` handles rows with only title (no priority or due_date).

'''

class Task:
    def __init__(self, title: str, priority: str = "medium", due_date: str | None = None):
        self.title:str = title
        self.priority:str = priority
        self.due_date:str | None = due_date
    
    @classmethod
    def from_dict(cls,data:dict)->"Task":
        priority = data.get("priority","medium")
        due_date = data.get("due_date",None)
        return cls(data["title"],priority,due_date)
    
    @classmethod
    def from_csv_row(cls,row:str)->"Task":
        parts = row.split(",")
        title=parts[0]
        priority=parts[1] if len(parts)>1 else "medium"
        due_date = parts[2] if len(parts)>2 else None
        return cls(title,priority,due_date)

    @classmethod
    def create_urgent(cls,title:str)->"Task":
        return cls(title,"critical","today")
    


if __name__ == "__main__":

    # Test 1: Normal initialization with defaults
    try:
        t = Task("Buy groceries")
        assert t.title == "Buy groceries"
        assert t.priority == "medium"
        assert t.due_date is None
        print("Test 1 passed: Default initialization works")
    except Exception as e:
        print(f"Test 1 failed: {e}")

    # Test 2: Normal initialization with all params
    try:
        t = Task("Meeting", "high", "2024-12-25")
        assert t.title == "Meeting"
        assert t.priority == "high"
        assert t.due_date == "2024-12-25"
        print("Test 2 passed: Full initialization works")
    except Exception as e:
        print(f"Test 2 failed: {e}")

    # Test 3: from_dict with all fields
    try:
        data = {"title": "Review code", "priority": "high", "due_date": "2024-12-20"}
        t = Task.from_dict(data)
        assert t.title == "Review code"
        assert t.priority == "high"
        assert t.due_date == "2024-12-20"
        print("Test 3 passed: from_dict with all fields works")
    except Exception as e:
        print(f"Test 3 failed: {e}")

    # Test 4: from_dict with only title (uses defaults)
    try:
        data = {"title": "Simple task"}
        t = Task.from_dict(data)
        assert t.title == "Simple task"
        assert t.priority == "medium"
        assert t.due_date is None
        print("Test 4 passed: from_dict with defaults works")
    except Exception as e:
        print(f"Test 4 failed: {e}")

    # Test 5: from_csv_row with all fields
    try:
        t = Task.from_csv_row("Deploy app,critical,2024-12-31")
        assert t.title == "Deploy app"
        assert t.priority == "critical"
        assert t.due_date == "2024-12-31"
        print("Test 5 passed: from_csv_row with all fields works")
    except Exception as e:
        print(f"Test 5 failed: {e}")

    # Test 6: from_csv_row with only title
    try:
        t = Task.from_csv_row("Quick task")
        assert t.title == "Quick task"
        assert t.priority == "medium"
        assert t.due_date is None
        print("Test 6 passed: from_csv_row with only title works")
    except Exception as e:
        print(f"Test 6 failed: {e}")

    # Test 7: from_csv_row with title and priority only
    try:
        t = Task.from_csv_row("Important task,high")
        assert t.title == "Important task"
        assert t.priority == "high"
        assert t.due_date is None
        print("Test 7 passed: from_csv_row with title+priority works")
    except Exception as e:
        print(f"Test 7 failed: {e}")

    # Test 8: create_urgent
    try:
        t = Task.create_urgent("Fix production bug")
        assert t.title == "Fix production bug"
        assert t.priority == "critical"
        assert t.due_date == "today"
        print("Test 8 passed: create_urgent works")
    except Exception as e:
        print(f"Test 8 failed: {e}")

    # Test 9: Verify all methods return Task instances
    try:
        t1 = Task.from_dict({"title": "A"})
        t2 = Task.from_csv_row("B")
        t3 = Task.create_urgent("C")
        assert isinstance(t1, Task)
        assert isinstance(t2, Task)
        assert isinstance(t3, Task)
        print("Test 9 passed: All classmethods return Task instances")
    except Exception as e:
        print(f"Test 9 failed: {e}")

    # Test 10: Edge case — empty CSV fields (potential issue)
    try:
        t = Task.from_csv_row("Task,,2024-12-25")  # Empty priority
        # Your code sets priority to "" (empty string), not "medium"
        if t.priority == "":
            print("Test 10 WARNING: Empty CSV field sets priority to '' not 'medium'")
        else:
            print("Test 10 passed")
    except Exception as e:
        print(f"Test 10 failed: {e}")

    print("\nAll tests completed!")