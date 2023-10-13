# 14. Write a program to understand the order of execution of methods in several base classes according to method resolution order (MRO).

class a1:
    def __init__(self):
        pass

class a2:
    def __init__(self):
        pass

class b(a1, a2):
    def __init__(self):
        pass

class c(b):
    def __init__(self):
        pass

class d(c):
    def __init__(self):
        pass

class e(d):
    pass

e1 = e()
print(e.mro())