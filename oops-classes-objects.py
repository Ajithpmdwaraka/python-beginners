class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding a new student to the database")
 
        
S1 = Student("Arjun", 98)
print(S1.name, S1.marks)   
        