# # Sets :- Sets are used to store multiple items in a single variable.
# It is a collection of object type element.
# It is denoted by {}
# It is mutable.
# It have no order.
# It is dynamic.
# It reduce duplicate value automatically.
# It is a class of collection.
# It is useful for mathematical opertaions.


## unordered collection of unique items

s = {1,2,3,4}
# print(s)
# print(s[1])   # error because it have no order

l = [1,2,3,4,4,4,4,4,4,5,5,5,5,1,1,1,2,4,7,89]
## how to remove duplicate value
# s2 = list(set(l))
# print(s2)

## pop method  
# s.pop()
# print(s)

## add method 
s.add("name")
print(s) 

## remove method
s.remove('name')  
# s.remove(6)    # error beacuse 6 is not present in s
print(s) 

## discard method (it does not give error if item is present or not) 
s.discard(6)   # no error
print(s)

## clear method 
# s.clear()
# print(s)

## copy method
s1 = s.copy()
print(s1)

s.update((5,5,67,8,8))
print(s)

