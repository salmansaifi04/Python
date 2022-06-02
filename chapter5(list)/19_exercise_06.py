# define a function that take a 2d or 3d list and return 1 if list is 2d and return 2 if 3d and so on...
# [1,2,3,[4,5,6]] ----> input
# 1  ----> output

def counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

num = [1,2,3,[4,5,6],[4,5,6],[4,5,6]] 
print(counter(num))