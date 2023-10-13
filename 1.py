# Write a program to swap two numbers without taking a temporary variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping :",a,b)

a,b = b,a

print("After swapping :",a,b)