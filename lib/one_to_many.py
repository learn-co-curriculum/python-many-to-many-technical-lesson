class Teacher:
    def __init__(self,name):
        self.name=name

    def students(self):
        return[student for student in Student.all_students if student.teacher==self]
    
    def add_student(self,student):
        if not isinstance(student,Student):
            raise TypeError('Student must be an instance of Student class')
        student.teacher=self

class Student:
    all_students=[]
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._teacher=None
        Student.all_students.append(self)

    @property
    def teacher(self):
        return self._teacher
    
    @teacher.setter
    def teacher(self,value):
        if not isinstance(value,Teacher):
            raise TypeError('teacher must be an instance of Teacher class')
        self._teacher=value


teacher1=Teacher('Mr.Johnson')

student1=Student('Alice',15,)
student2=Student('Bob',14)
student3=Student('Faith',16)

teacher1.add_student(student1)
teacher1.add_student(student2)
teacher1.add_student(student3)

for student in teacher1.students():
    print(student.name)

print(teacher1.students())