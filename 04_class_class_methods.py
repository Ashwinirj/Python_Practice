class Student:

    school = "Telusko "

    def __init__(self, m1,m2,m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)//3 
    
    @classmethod
    def getSchoolname(cls):  #accessing class variables
        return cls.school
        


Raj = Student(50,70,80)
Manish = Student(90,98,96)

# print(f"Student Raj marks are {Raj.m1, Raj.m2, Raj.m3}")
# print(f"Student Manish marks are {Raj.m1, Raj.m2, Raj.m3}")

# print("Average of marks are ", Raj.avg())
# print(Raj.getSchoolname())

print(Student.getSchoolname())  #TypeError: Student.getSchoolname() missing 1 required positional argument: 'cls'
