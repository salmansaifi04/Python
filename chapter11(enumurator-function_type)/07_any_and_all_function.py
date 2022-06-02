# any , all function

numbers1 = [2,4,6,8,10]
numbers2 = [2,4,5,7,9]

## any and all function with list comprehension
print(all([i%2==0 for i in numbers1]))   # Output ---> True  
print(all([i%2==0 for i in numbers2]))   # Output ---> False  


print(any([i%2==0 for i in numbers1]))   # Output ---> True  
print(any([i%2==0 for i in numbers2]))   # Output ---> True



## how to check even numbers
evens = []
for i in numbers1:
    evens.append(i%2==0)
# print(evens)

## using all function
# print(all([True, True, True, True, True]))   # it gives True
# print(all([True, False, True, True, True]))   # it gives False

## using any function
# print(any([True, False, False, False, False]))   # it gives True if any one is True
# print(all([False, False, False, False, False]))   # it gives False if every one is False