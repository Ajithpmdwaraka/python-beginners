class Student:
    college_name = "Cochin University"
    
    def __init__(self, name, department):
        self.name = name
        self.department = department
        print("This is the list of students")
        
    def add_student(self):
        return self.name
        
        
S1 = Student("Ajith", "Computer Science")
print(S1.name, S1.department)

print(S1.add_student())
        
        
        
        
