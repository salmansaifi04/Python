## In the above function we add the (*args, **kwargs) to take the any number of argument
## And we also return the any_function 

def decorator_function(any_function):
    def inner_function(*args, **kwargs):
        print("This is awesome")
        return any_function(*args, **kwargs)
    return inner_function

@decorator_function
def func(a):
    print(f"This is function with argument {a}")

func(3)

@decorator_function
def add(a,b):
    return a+b
print(add(2,3))