# 6. Write a program to create Student class with a constructor having more than one parameter.

class Student:
    def __init__(self, name, div):
        self.name = name
        self.div = div
    
    def display(self):
        print(f"Student {self.name} is studying in {self.div} division.")

s1 = Student("Mihir", "B")
s1.display()