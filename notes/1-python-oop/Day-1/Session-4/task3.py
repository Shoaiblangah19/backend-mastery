'''
### ⚡ Micro Task 3 (5 min)

Create a `Student` class with name and a `grades` list. Create a `Classroom` class that has a name and a list of students.

Create 3 students. Add 2 of them to Classroom A, and 2 of them to Classroom B (one student should be in BOTH classrooms).

Add a grade to the shared student. Print grades from both classrooms to verify that the shared student's grade shows up in both — because it's the same object.
'''

class Student:
    def __init__(self,name:str):
        self.name:str = name
        self.grades:list = []

class Classroom:
    def __init__(self,name:str):
        self.name:str = name
        self.students_list:list[Student]=[]
    
student1=Student("Shoaib")
student2=Student("Javaid")
student3=Student("Sohail")

room1=Classroom("Learning")
room2=Classroom("Earning")
room1.students_list.append(student1)
room1.students_list.append(student2)

room2.students_list.append(student1)
room2.students_list.append(student2)

student1.grades.append(12)
print(room1.students_list[0].grades)
print(room2.students_list[0].grades)