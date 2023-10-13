# 13. Write a python program that asks the user to enter a length in centimeters. If the user enters a negative length, the program should tell the user that the entry is invalid. Otherwise, the program should convert the length to inches and print out the result.

a = float(input("Enter CM: "))

if a<0:
    print("Invalid length!")
else:
    print(a/2.54)