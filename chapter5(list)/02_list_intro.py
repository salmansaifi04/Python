# list :- It is orderd collection of items
# you can store anything in list int, float, string

numbers = [1,2,3,4]
print(numbers)

words = ['one', 'two', 'three', 'four']
print(words)

mixed = [1,2.0,'three',None]
print(mixed)

# how to access the element from the list
print(numbers[1])
print(numbers[-1])

# slicing
print(words[:2])
print(words[0:])
print(words[:4])
print(words[::-1])

# how to change data 
mixed[1] = 'two'
print(mixed)

words[1:] = 'two'
print(words)

words[1:] = [1,2]
print(words)