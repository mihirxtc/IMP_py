# 16. Write a program to handle multiple exceptions like SyntaxError and TypeError.

try:
    a = eval("Jack is Best")
    b = 1 + "2"

except(SyntaxError):
    print("Can't evaluate a string")
    
except(TypeError):
    print("Can't join a string to int")