# more about get method 

user = {'name' : 'salman', 'age' : 21}
print(user.get('names', 'not found'))  # if names not found in user then it print 'not found'

# two same keys in dictionaries

user1 = {'name' : 'salman', 'age' : 19, 'age' : 21}  # 21 override 19
print(user1)