# 4. Write a program to handle some built in exceptions like ZeroDivisionError.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    print(a/b)
except(ZeroDivisionError):
    print("Can't Divide by zero")