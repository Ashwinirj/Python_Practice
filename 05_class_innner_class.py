class Student:

    def __init__(self,name,age,department):
        self.name = name  
        self.age = age 
        self.department = department
        self.lap = self.Laptop("HP","15",8)
    
    def show(self):
        print(self.name, self.age, self.department)
        self.lap.show()


    class Laptop:

        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram

        def show(self):
            print(self.brand, self.cpu, self.ram)
            


    
s1 = Student("Ashwini",30,"CSE")
s2 = Student("Shweta",32,"MCA")

s2.lap1 = Student.Laptop("Lenovo","17", 16)

s1.show()
s2.show()
s2.lap1.show()