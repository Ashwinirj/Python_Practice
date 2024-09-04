class A:
    def __init__(self):
        self.name = "Ashwini"
        self.age = 30 
    
    def update(self):
        self.age = 35

    

A = A()

A.name = "Ashu"

A.age = 40 

A.update()

print(f" Name is {A.name} age is {A.age}")
