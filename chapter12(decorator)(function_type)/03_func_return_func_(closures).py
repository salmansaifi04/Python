## function returning function  (closures, first class function)

# example 1
def outer_func():
    def inner_func():
        print("inside inner func")
    return inner_func

var = outer_func()    
var()


# example 2

def outer_func2(msg):
    def inner_func2():
        print(f"message is {msg}")
    return inner_func2

var2 = outer_func2("hello")
var2()