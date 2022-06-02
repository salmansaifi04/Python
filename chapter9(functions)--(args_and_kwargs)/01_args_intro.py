# *args 

def func(*args):
    print(args)   # it print tuple
    print(type(args))

func(1,2,3,4,5,6,4)

def add_all(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add_all(1,2,3,4,6,8,11,23))