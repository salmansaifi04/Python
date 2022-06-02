def greater(a,b):
    if a>b:
        return a
    else:
        return b

def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c


# function inside function 

# first method
def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger, c)
print(new_greatest(4,5,3))

# second method 
def new_greatest1(a,b,c):
    return greater(greater(a,b), c)
print(new_greatest1(4,5,3))



# programming_principle :- kiss ----> keep it simple stupid