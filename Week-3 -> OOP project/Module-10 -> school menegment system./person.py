import random
from school import School

class parson:
    def __init__(self,name):
        self.name = name

class Teacher(parson):
    def __init__(self, name):
        super().__init__(name)
    
    def evaluate_exam(self):
        return random.randint(1,100)
    
class Student(parson):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {} #{math : 80}
        self.grade = {} # { math : a+}
        self.subject_grade = {} # { math : a+} 
    
    def final_grade(self):
        sum = 0
        for grade in self.grade.values():
            point = School.grade_to_value(grade)
            sum += point
        gpa = sum / len(self.grade) 
        self.subject_grade = School.Value_to_grade(gpa)
    
    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id = value
    

