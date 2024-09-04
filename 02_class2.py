class Computer:
    def __init__(self):
        self.name = "Ashwini"
        self.age = 30 
    
    def compare(self, other):
        if self.age == other.age:
            print('SAME')
        else:
            print("Diff")
    


P1 = Computer()
# P1.age = 45
P2 = Computer()

P1.compare(P2)


