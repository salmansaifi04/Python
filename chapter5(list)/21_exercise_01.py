# define a function that take list of string as a argument and
# return list containing reverse of every string

# example 
# input :-  l = ['abc', 'tuv', 'wxy']
# output :- ['cba', 'vut', 'yxw']



# def reverse_string(l):
#     output = []
#     for i in l:
#         output.append(i[::-1])
#     print(output)

# reverse_string(l)


#### list comprehension ####

l = ['abc', 'tuv', 'wxy']
def rev_string(l):
    return [i[::-1] for i in l]

print(rev_string(l))