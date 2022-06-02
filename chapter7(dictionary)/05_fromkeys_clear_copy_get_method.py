## **** fromkeys (with the help of this method we can create a dict which has the same 'value' of different key)
# for example :- 
# d = {'name' : 'unknown', 'age' : 'unknown'}   

d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
d1 = dict.fromkeys(('name', 'age', 'height'), 'unknown')
d2 = dict.fromkeys(range(1,11), 'unknown')
d3 = dict.fromkeys("abc", 'unknown')
d4 = dict.fromkeys(['name', 'age', 'height'], ['unknown','unknown','unknown'])


print(f"with the help of list : {d}")
print(f"with the help of tuple : {d1}")
print(f"with the help of range function : {d2}")
print(f"with the help of string : {d3}")
print(f"add three value to a key : {d4}")

## **** get method (it does not give error if we pass a key which is not present)
user = {'name' : 'salman', 'age' : 21}
print(user.get('name'))     # no error
print(user.get('names'))    # no error (it return none if key us not present)


# if 'name' in user:
#     print("Present")
# else:
#     print("Not present")

# shortcut
if d.get('name'):
    print("Present")
else:
    print("Not Present") 

## **** clear method ****

# user.clear()
# print(user) 

## **** copy method ****
d1 = user.copy()
print(d1)
# print(d1.popitem())
# print(user)    # original dictionary do not change
# print(d1)      


## how to check dict is same or not ##
print(user is d1) 