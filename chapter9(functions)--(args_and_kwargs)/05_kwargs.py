# kwargs (keyword argument)
# **kwargs (double star operator)
# it is used for dictionary


# kwargs as parameter
def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))   # type is dict
    for k,v in kwargs.items():
        print(f"{k} : {v}")

func(first_name = 'Salman', last_name = 'Saifi')

# dictionary unpacking
d = {'first_name' : 'Salman', 'last_name' : 'Saifi'}
func(**d)  # no error
# func(d)  # error

# kwargs with normal parameter

def func1(num, **kwargs):
    print(num)
    print(kwargs)

# func1(first_name = 'salman', last_name = 'saifi')   # error
func1(2,first_name = 'salman', last_name = 'saifi')   # no error