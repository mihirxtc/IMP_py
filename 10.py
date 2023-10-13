# 10. Write a program to implement single inheritance in which two sub classes are derived from a single base class.

class Parent1:
    p_num = 50

class Child1(Parent1):
    def __init__(self):
        self.c_num = 30

class Child2(Parent1):
    def __init__(self):
        self.c_num = 20

c1 = Child1()
print(f"child class number = {c1.c_num}, parent class number = {c1.p_num}")

c2 = Child2()
print(f"child class number = {c2.c_num}, parent class number = {c2.p_num}")