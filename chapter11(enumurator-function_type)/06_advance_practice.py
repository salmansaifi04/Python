# define a function that take any number of lists containing numbers
# [1,2,3], [4,5,6], [7,8,9]
# return average
# (1+4+7)/3, (2+5+7)/3, (3+6+9)/3

def average_finder(*args):
    new_list = []
    for pair in zip(*args):
        new_list.append(sum(pair)/len(pair))
    return new_list

print(average_finder([1,2,3], [4,5,6], [7,8,9]))


# lambda function

average = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(average([1,2,3], [4,5,6], [7,8,9]))