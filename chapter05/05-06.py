def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

print(dir(factorial))

class C:
    pass

obj = C()

def func():
    pass

print(set(dir(func)) - set(dir(obj)))



