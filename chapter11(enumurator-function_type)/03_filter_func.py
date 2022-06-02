# filter function

# is_even function

# first method
numbers = [4,6,5,2,3,7,8,10]
is_even = list(filter(lambda a:a%2==0, numbers))
print(is_even)

# second method 
is_even = filter(lambda a:a%2==0, numbers)
for i in is_even:
    print(i)

# using list comprehension

is_even2 = [i for i in numbers if i%2==0]
# print(is_even2) 