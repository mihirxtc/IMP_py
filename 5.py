# 5. Write a program to find out and display the common and the non common elements in the list using membership operators.

list1 = [10, 20, 30, 40, 50, "Mihir", "xyz"]

a = input("Enter first element: ")
b = input("Enter second element: ")
c = input("Enter third element: ")

if a in list1:
    print(f"{a} is in list1")
else:
    print(f"{a} is not in list1")

if b in list1:
    print(f"{b} is in list1")
else:
    print(f"{b} is not in list1")

if c in list1:
    print(f"{c} is in list1")
else:
    print(f"{c} is not in list1")