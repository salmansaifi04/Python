# generate list with a range function
numbers = list(range(1,11))
print(numbers)

# pass list to a function
def negative_list(l):
    output = []
    for i in l:
        output.append(-i)
    return output

print(negative_list(range(1,11)))