class Student:
    def __init__(self,name,mark):
        self.name = name
        self.mark = mark
    
    def get_result(self):
        if self.mark >= 50:
            return f"{self.name} has passed the exam"
        else:
            return f"{self.name} has failed the exam"