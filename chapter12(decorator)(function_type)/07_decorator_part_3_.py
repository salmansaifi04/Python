## in the above function we use 'wraps' from 'functools' to print the doc string of the add function without 'wraps' we cannot print the add doc string here when we call the add.__doc__ then it print the 'This is inner function'

from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def inner_function(*args, **kwargs):
        '''This is inner function'''
        print("This is awesome")
        return any_function(*args, **kwargs)
    return inner_function


@decorator_function
def add(a,b):
    '''this is add function'''
    return a+b

print(add.__doc__)
print(add.__name__)