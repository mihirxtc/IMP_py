# 18. Write a program to create a static method that counts the number of instances created for a class.

class Class1:
    n1 = 0
    def __init__(self):
        Class1.n1+=1

    @staticmethod
    def display():
        print(Class1.n1)

c1 = Class1()
Class1.display()