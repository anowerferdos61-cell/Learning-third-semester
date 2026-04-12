class Student:
    def __init__(self, name, attendance):
        self.name = name
        self.attendance = attendance
        self.marks = 0
    
    def mark_attendance(self):
        self.attendance += 1
        print(f"{self.name} has attended {self.attendance} classes.")
    def add_marks(self, marks):
        if self.attendance >= 75:
            self.marks += marks
        else:
            print(f"{self.name} has not attended enough classes to receive marks.") 

student1 = Student("Anower", 74)
student2 = Student("Rahim", 70)
student3 = Student("Karim", 90)

student1.mark_attendance()
student1.add_marks(85)
print(f"{student1.name} has {student1.marks} marks.\n")

student2.mark_attendance()
student2.add_marks(90)
print(f"{student2.name} has {student2.marks} marks.\n")

student3.mark_attendance()
student3.add_marks(95)
print(f"{student3.name} has {student3.marks} marks.\n")