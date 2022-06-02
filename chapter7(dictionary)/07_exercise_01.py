# define a function that takes a number(n)
# return a dictionary containing cube of a numbers from 1 to n

# example
# cube_finder(3)
# {1:1, 2:8, 3:27}


def cube_finder(n):
    output = {}
    for i in range(1,n+1):
        output[i] = i**3
    return output
print(cube_finder(3))