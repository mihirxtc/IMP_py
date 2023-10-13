# 17. Write a program to search an element in the list using for loop and also demonstrate the use of else suite with for loop.

def search_element(lst, target):
    for item in lst:
        if item == target:
            print(f"Element {target} found in the list")
            break
        else:
            print(f"Element {target} is not found in the list.")

my_list = [10, 20, 30, 40, 50]
element_to_search = 10

search_element(my_list, element_to_search)