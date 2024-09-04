class Car:

    wheels = 4 #CLASS VARIABLE or STATIC Variables 

    def __init__(self):
        self.mil = 15        # INSTANCE variable 
        self.com = "Ford "   # INSTANCE variable 


c1 = Car()
print( c1.mil, c1.com, c1.wheels)  # using object name to access class variables
c2 = Car()
c2.com = "BMW"
print( c2.mil, c2.com, Car.wheels)  # using CLASS name to access the class variables 
        