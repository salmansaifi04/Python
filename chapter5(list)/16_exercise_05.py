# common element finder function
# define a function that take two list as a input and return a list
# which contains common elements of both lists

# example 
# input ----> [1,2,3,4], [1,2,5,6]
# output ---> [1,2]


def func(l1,l2):
    empty_list = []
    for i in l1:
        for j in l2:
            if i == j:
                empty_list.append(i)
    return empty_list

l1 = [1,2,3,4]
l2 = [1,2,5,6]
print(func(l1,l2))



# second method
def func1(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

print(func1(l1,l2))