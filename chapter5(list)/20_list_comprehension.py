## list comprehension
## with the help of list comprehension we can create list in a one line

### ---- example1 ---- ##
## create a list of square from 1 to 10
l = []
for i in range(1,11):
    l.append(i**2)
print(l)


## create a list of square from 1 to 10 (with the help of list comprehension)

l1 = [i**2 for i in range(1,11)]
print(l1)

### ---- example2 ---- ###
## negative values program
neg_val = []
for i in range(1,11):
    neg_val.append(-i)
print(neg_val)

## list comprehension
neg_val1 = [-i for i in range(1,11)]
print(neg_val1)


### ---- example3 ---- ###
names = ["Salman", "Prakash", "Suraj"]
new_list = []
for i in names:
    new_list.append(i[0])
print(new_list)

### list comprehension
names1 = [i[0] for i in names]
print(names1)


