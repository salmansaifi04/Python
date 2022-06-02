# map function

number = [1,2,3,4]

## using map function
squares = list(map(lambda a:a**2, number))
print(squares)

## list comprehension
square_new = [i**2 for i in number]
print(square_new)

## simple way

new_list = []
for i in number:
    new_list.append(i**2)
print(new_list) 

## another example
names = ["abc", "abcdef", "abcd"]
length = map(len, names)
for i in length:
    print(i)