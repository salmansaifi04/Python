# compare list
# ==, is

fruits1 = ['apple', 'banana', 'orange' ]
fruits2 = ['pear', 'kiwi', 'apple', 'banana']
fruits3 = ['apple', 'banana', 'orange' ]

# print(fruits1 == fruits2)   # gives False
print(fruits1 == fruits3)   # gives True (because values are same)

print(fruits1 is fruits3)   # it check same memory location (gives error)