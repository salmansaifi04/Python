# Tuples :- It is denoted by ()
# It is a static
# It is faster than list
# It is a class of collection
# It can store any type of data
# **** most important **** tuples are immutable, once tuple is created you can't update
# no update, no insert, no pop, no remove


example = ( 3, 'two', 3, 4)
print(example)

## **** method to be used ****
## 1. count method
print(example.count(3))

## 2. index method
print(example.index('two'))

## 3. len function
print(len(example))

# slicing
# print(example[:2])
# print(example[::-1])

## we cannot change item
# example[0] = 1         # error
# print(example)         # error