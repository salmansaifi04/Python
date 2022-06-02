##### how to pass a function inside a function #####
## ---- map function ---- ##

def square(a):
    return a**2

l = [1,2,3,4]

print(list(map(square, l)))

## using lambda expression
print(list(map(lambda a:a**2, l)))


## ---- how to define a my map function ---- ##
def my_map(func, l):
    new_list = []
    for i in l:
        new_list.append(func(i))
    return new_list


print(my_map(square, l))

## using lambda expression
print(my_map(lambda a:a**2, l))

## using list_comprehension

def my_map2(func, l):
    return [func(i) for i in l]

print(my_map2(lambda a:a**2, l))
