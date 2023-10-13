# 2. Write a program to create Student class with name, age and marks as data members. Also create a method named display() to view the student details. Create an object to Student class and the method using object.

class Student:
    name = "Mihir"
    age = 20
    marks = 50

    def display(self):
        print("Name:",self.name,"\nAge:",self.age,"\nMarks:",self.marks)

s1 = Student()
s1.display()