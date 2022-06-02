# function returning two values

def func(x,y):
    add = x+y
    mul = x*y
    return add, mul

print(func(2,3))    # it return tuple


# but we can store in a two diiferent variable 
add, mul = func(5,6)
print(add)
print(mul)