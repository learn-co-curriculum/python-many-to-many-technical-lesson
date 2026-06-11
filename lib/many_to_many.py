class Student:
    all =[]
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Student.all.append(self)

    def courses(self):
        return[schedule.course for schedule in Schedule.all if schedule.student==self]
    
    def calculate_gpa(self):
        grades=[schedule.grade for schedule in Schedule.all if schedule.student==self]
        return sum(grades)/len(grades)

class Course:
    all =[]
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        Course.all.append(self)

    def students(self):
        return[schedule.student for schedule in Schedule.all if schedule.course==self]

class Schedule:
    all=[]
    def __init__(self,student,course,grade):
        self.student=student
        self.course=course
        self.grade=grade
        Schedule.all.append(self)
    @property
    def student(self):
        return self._student
    @student.setter
    def student(self,value):
        if not isinstance(value,Student):
            raise Exception
        self._student=value

    @property
    def course(self):
        return self._course
    @course.setter
    def course(self,value):
        if not isinstance(value,Course):
            raise Exception
        self._course=value
    

alice=Student('Alice','alice@gmail.com')
grace=Student('Grace','grace@gmail.com')

py=Course('Intro to python','Mr.Son')
oop=Course('OOP Python','Mrs.Berge')

Schedule(alice,py,3.8)
Schedule(grace,oop,3.85)
Schedule(alice,oop,3.5)
Schedule(grace,py,3.4)

print(alice.courses())
print (grace.calculate_gpa())

for student in py.students():
    print(student.name)