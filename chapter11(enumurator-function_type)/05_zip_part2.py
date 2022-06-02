# zip part 2

l = [(1,2),(3,4),(5,6),(7,8)]

## * operator with zip function
# how to convert l to l1,l2

l1,l2 = list(zip(*l))
print(l1)   # tuple
print(l2)   # tuple

print(list(l1))   # list
print(list(l2))   # list


## max function with zip function

l1 = [1,3,5,7]
l2 = [2,4,6,8]

new_list = []
for pair in zip(l1,l2):
    new_list.append(max(pair))
print(new_list) 