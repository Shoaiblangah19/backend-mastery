'''
### ⚡ Micro Task 2 (7 min)

Create a `Student` class with name, grades (list of numbers), and attendance percentage.

Write these simple methods first:
- Get average grade
- Is passing (average grade >= 50)
- Has good attendance (attendance >= 75%)

Then write one complex method using the simple ones:
- Get student report: returns a string with name, average, pass/fail status, and attendance status

The report method should call the other three methods, not recalculate anything itself.

Test with 2 students — one passing with good attendance, one failing with poor attendance.
'''

class Student:
    def __init__(self,name:str,grades:list[int],attendence:int):
        self.name:str = name
        self.attendence:int = attendence
        self.grades:list[int] = grades
    
    def get_average(self)->int:
        if len(self.grades)==0:
            return 0
        return sum(self.grades,0)/len(self.grades)
    
    def is_passing(self)->str:
        return "Pass" if self.get_average()>=50 else "Fail"
    
    def has_good_attendance(self)->str:
        return "Good" if self.attendence >=75 else "Poor"
    
    def get_report(self)->str:
        return f"Name: {self.name}\nAverage: {self.get_average():.2f}\nResult: {self.is_passing()}\nAttendance: {self.has_good_attendance()}"

 
# Test cases
if __name__ == "__main__":
    # Student 1: Passing with good attendance
    student1 = Student("Alice", [85, 90, 78], 85)
    report1 = student1.get_report()
    expected1 = "Name: Alice\nAverage: 84.33\nResult: Pass\nAttendance: Good"
    assert report1 == expected1, f"Test failed for student1:\nExpected:\n{expected1}\nGot:\n{report1}"
    
    # Student 2: Failing with poor attendance
    student2 = Student("Bob", [45, 30, 40], 70)
    report2 = student2.get_report()
    expected2 = "Name: Bob\nAverage: 38.33\nResult: Fail\nAttendance: Poor"
    assert report2 == expected2, f"Test failed for student2:\nExpected:\n{expected2}\nGot:\n{report2}"
    
    # Edge case: Empty grades list
    student3 = Student("Charlie", [], 90)
    report3 = student3.get_report()
    expected3 = "Name: Charlie\nAverage: 0.00\nResult: Fail\nAttendance: Good"
    assert report3 == expected3, f"Test failed for student3:\nExpected:\n{expected3}\nGot:\n{report3}"
    
    # Edge case: Exactly 50 average (passing threshold)
    student4 = Student("Diana", [50, 50, 50], 75)
    report4 = student4.get_report()
    expected4 = "Name: Diana\nAverage: 50.00\nResult: Pass\nAttendance: Good"
    assert report4 == expected4, f"Test failed for student4:\nExpected:\n{expected4}\nGot:\n{report4}"
    
    # Edge case: Attendance exactly 75% (good attendance threshold)
    student5 = Student("Eve", [60, 70, 80], 75)
    report5 = student5.get_report()
    expected5 = "Name: Eve\nAverage: 70.00\nResult: Pass\nAttendance: Good"
    assert report5 == expected5, f"Test failed for student5:\nExpected:\n{expected5}\nGot:\n{report5}"
    
    print("All tests passed!")
