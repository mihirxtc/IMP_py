# 19. Write a program to convert the elements of two lists into key-value pair of a dictionary.

a = ["key1", 83, "key2"]
b = ["Mihir", "xyz", 99]

my_dict = dict(zip(a, b))
print(type(my_dict), my_dict)