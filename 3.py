# 3. Write a program to understand various methods of array class mentioned: append, insert, remove, pop, index, tolist and count.

import array as a

arr1 = a.array("i", [10, 20, 30, 40, 50])
print(arr1)

arr1.append(70)
print(arr1)

arr1.insert(5, 60)
print(arr1)

arr1.remove(70)
print(arr1)

arr1.pop(5)
print(arr1)

arr1.remove(10)
print(arr1)

print(arr1.index(20))

list1 = list(arr1)
print(list1)

print(arr1.count(50))