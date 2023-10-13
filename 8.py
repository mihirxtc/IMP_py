# 8. Write a program to import "os" module to the current working directory and returns a list of all module functions.

import os

function = dir(os)
for i in function:
    print(i)