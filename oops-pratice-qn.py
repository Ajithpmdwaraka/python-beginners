class Student:
    
    def __init__(self, name, english, maths, hindi):
        self.name = name
        self.english = english
        self.maths = maths
        self.hindi = hindi
    
    def average_marks(self):
        average = (self.english + self.maths + self.hindi)/3
        return average
    

s1 = Student("Ajith", 20, 30, 40)
print(s1.average_marks())      