from functools import wraps

def print_function_data(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"You are calling {function.__name__} function")
        print(function.__doc__)
        return function(*args, **kwargs)
    return wrapper

@print_function_data
def add(a,b):
    '''This function takes two numbers as arguments and return their sum'''
    return  a+b

print(add(5,4))
# output
# you are calling add function
# This function takes two numbers as arguments and return their sum
# 9