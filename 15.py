# 15. Create a sample list of 7 elements and implement the list methods mentioned: append, insert, copy, extend, count, remove, pop, sort, reverse and clear.

list1 = [10, 20, 30, 40, 50, 60, 70]
print(list1)

list1.append(90)
print(list1)

list1.insert(7, 80)
print(list1)

list2 = list1.copy()
print(list2)

new_list = [100, 110, 120]
list1.extend(new_list)
print(list1)

print(list1.count(100))

list1.remove(120)
print(list1)

list1.pop(9)
print(list1)

print(list1.sort())

list1.reverse()
print(list1)

list1.clear()
print(list1)