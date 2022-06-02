# we use enumurate function with for loop to track the position of our item in iterable


# How can we do this without enumurate function
l = ["a","b","c"]
pos = 0
for i in l:
    print(f"{pos} ----> {i}")
    pos += 1

# with enumurate function
l1 = ["A", "B", "C"]
for i, j in enumerate(l1):
    print(f"{i} ----> {j}")


# Define a function that take two arguments
# 1. list containing one argument
# 2. string that want to find in your list
# and this function will return the index of string in your list and is string is not present then return -1


def find_pos(l, target):
    for pos,name in enumerate(l):
        if name == target:
            return pos
    return -1

print(find_pos(l1, "C"))