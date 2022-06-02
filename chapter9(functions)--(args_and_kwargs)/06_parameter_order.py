# function with all type of parameter

# PADK

# parameters
# *args
# default parameter
# **kwargs

def func(name, *args, last_name='unknown', **kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func("salman",1,2,3,4,first_name = 'salman', age = 21)
