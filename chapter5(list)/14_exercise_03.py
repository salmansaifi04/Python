# define a function that take list of words as argument and
# return list with reverse of every element in that list

# example :
# ['abc','xyz','tuv']  ---> ['cba', 'zyx', 'vut']

def reverse_item(l):
    r_list = []
    for i in l:
        r_list.append(i[::-1])
    return r_list

l = ['abc','xyz','tuv']
print(reverse_item(l))