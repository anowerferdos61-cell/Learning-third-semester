class School:
    def __init__(self,s_name,s_addr,):
        self.name = s_name
        self.address = s_addr
        self.teachers = {} # {"key = subject" : "value = teacher_name"}
        self.classrooms = {} # {"class eight , teacher = teacher name"}
    
    def add_classroom(self,classroom):
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self,subject,teacher):
        self.teachers[subject.name] = teacher
        
    def student_admission(self,student):
        class_name = student.classroom.name
        self.classrooms[class_name].add_student(student)



    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >= 60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks < 60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        else:
            return "F"
    
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def Value_to_grade(value):
        if value >= 5.00:
            return 'A+'
        elif value>=4.00 and value<5.00:
            return 'A'
        elif value>= 3.50 and value<4.00:
            return 'A-'
        elif value >= 3.00 and value < 3.50:
            return 'B'
        elif value >= 2.00 and value < 3.00:
            return 'C'
        elif value >= 1.00 and value < 2.00:
            return 'D'
        else:
            return 'F'
    
    def __repr__(self):
         # All Classrooms
        print("--All classes--")
        for key in self.classrooms.keys():
            print(key)
        # All Students
        print("All Students")
        result = ''
        for key,value in self.classrooms.items(): # prottekta classroom e gelam
            result += f"---{key.upper()} Classroom Students\n"
            for student in value.students:
                result += f"{student.name}\n"
        print(result)

        # All Subjects
        subject = ''
        for key,value in self.classrooms.items(): # prottekta classroom e gelam
            subject += f"---{key.upper()} Classroom Subjects\n"
            for sub in value.subjects:
                subject += f"{sub.name}\n"
        print(subject)
        # All Teachers - Homework
        print("--All Teachers--")
        for key,value in self.teachers.items():
            print(f"{key}: {value.name}")
    
        # All Student Results
        print("Students Results")
        for key,value in self.classrooms.items():
            for student in value.students:
                for k,i in student.marks.items():
                    print(student.name,k,i,student.grade[k],student.classroom.name)
                print(student.subject_grade)
        return ''