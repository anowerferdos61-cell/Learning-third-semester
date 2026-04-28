from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School("dhaka collage" , "dhaka")

#  classroom object
eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

#add classroom 
school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)

# teacher object
anower = Teacher("Anower")
ferdos = Teacher("Ferdos")
asha = Teacher("Asha")
karim = Teacher("Karim")
fatima = Teacher("Fatima")

chem = Subject('chemistry',anower)
math = Subject('math',ferdos)
eng = Subject('english',asha)
bangla = Subject('bangla',karim)
physics = Subject('physics',fatima)

school.add_teacher(chem,anower)
school.add_teacher(math,ferdos)
school.add_teacher(eng,asha)
school.add_teacher(bangla,karim)
school.add_teacher(physics,fatima)

# add subject
nine.add_subject(chem)
nine.add_subject(bangla)
ten.add_subject(math)
ten.add_subject(physics)
eight.add_subject(eng)
eight.add_subject(bangla)

# student object 
s1 = Student('Samira',eight)
s2 = Student('mira',eight)
s3 = Student('Saira',nine)
s4 = Student('paira',nine)
s5 = Student('aira',nine)
s6 = Student('Rahim',eight)
s7 = Student('Hassan',ten)
s8 = Student('Zara',nine)
s9 = Student('Rima',eight)
s10 = Student('Tariq',ten)

#add stiudent
school.student_admission(s1)
school.student_admission(s2)
school.student_admission(s3)
school.student_admission(s4)
school.student_admission(s5)
school.student_admission(s6)
school.student_admission(s7)
school.student_admission(s8)
school.student_admission(s9)
school.student_admission(s10)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)