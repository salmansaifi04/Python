# append method

fruits1 = ['apple', 'mango']
fruits1.append('grapes')
print(fruits1)

# insert method
fruits2 = ['mango', 'orange']
fruits2.insert(1, "apple")
print(fruits2)

# how to join (concatenate) two list
fruits = fruits1 + fruits2
print(fruits)

# extend method 
fruits1.extend(fruits2)
print(fruits1)
print(fruits2)

# diffrence between extend and append method
fruits2.append(fruits1)   # list inside list
print(fruits2)
