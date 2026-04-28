from person import Teacher
from school import School

class Subject:
    def __init__(self,name,teacher):
        self.name = name
        self.teacher = teacher
        self.max_mark = 100
        self.pass_mark = 33
    
    def exam(self,students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.grade[self.name] = School.calculate_grade(mark)


