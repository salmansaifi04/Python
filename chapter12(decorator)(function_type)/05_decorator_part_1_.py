## Decorators :- Enhance the functionality of the other function
# @ is used for decorator

def decorator_function(any_function):
    def inner_function():
        print("This is awesome")
        any_function()
    return inner_function


# this is awesome
@decorator_function
def func1():
    print("This is function 1")
    
func1()

# this is awesome
@decorator_function
def func2():
    print("This is function 2")

func2()
