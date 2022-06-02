# *args with normal parameter

def func(num, *args):
    print(num)
    print(args)

func(1,2,3,4,56,33,44)   #no error
func()   # error

# in the above function we have to pass at least one argument if we don't pass it gives error