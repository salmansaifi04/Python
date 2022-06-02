## lambda function practice

## example 1 (odd_even)

def is_even(a):
    return a%2==0
# print(is_even(6))

is_even2 = lambda a : a%2==0
# print(is_even2(5))

## example 2 (last_char)
def last_char(s):
    return s[-1] 
# print(last_char("salman"))

last_char2 = lambda s:s[-1]
# print(last_char2("salman"))

## lambda with if, else statement

def func(name):
    if len(name)>5:
        return True
    return False

func2 = lambda name: True if len(name)>5 else False
# print(func2("salman"))    

# another method to solve the above problem

func3 = lambda s:len(s)>5
# print(func3("salman"))