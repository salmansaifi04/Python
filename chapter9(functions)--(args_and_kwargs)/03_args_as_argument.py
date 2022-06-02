# *args as argument

def multiply_nums(*args):
    multiply = 1
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums(2,3,4))   

# if we have to pass a list to a function

l = [2,3,4]
print(multiply_nums(l))    # it takes list as a argument and output is [2,3,4] not 24

# but if 
print(multiply_nums(*l))   # it is correct