fruits = ['apple', 'banana', 'orange', 'pear', 'kiwi', 'apple', 'banana']

## count method
print(fruits.count('apple'))

## sort method 
fruits.sort()
print(fruits)
numbers = [2,1,4,3,6,2]
# numbers.sort()
# print(numbers)

## sorted function 
print(sorted(numbers))
print(numbers)

## reverse method
numbers.reverse()
print(numbers)

## clear method 
numbers.clear()
print(numbers)

## copy method
## Two types of copy:-
# 1. sallow copy (change)
# 2. deep copy (not change)


l = [3,4,5,6]
l2 = []
l2 = l.copy()
print(l2)


# index method
num1 = [1,2,3,4,5,6,7,1,3,4,5,1]
print(num1.index(1))
print(num1.index(1, 3))
print(num1.index(1, 3, 7))
# first argument is list item name,
# second argument is where to start
# third argument is where to stop





