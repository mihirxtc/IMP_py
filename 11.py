# 11. Write a lambda/Anonymouse function to find bigger number in given numbers

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

maxNum = lambda x,y:x if x>y else y

print(f"Bigger number in {x} and {y} is {maxNum(x, y)}")