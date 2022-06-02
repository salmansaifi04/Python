# list comprehension in nested list

# example = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

nested_list = [[i for i in range(1,4)] for j in range(1,4)]
print(nested_list)
