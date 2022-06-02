# zip function
user_id = ['user1', 'user2', 'user3']
first_name = ['salman', 'prakash', 'suraj']
last_name = ['saifi', 'singh', 'sharma']

# if we have a zip function whose has two list then we can convert it to the dict 
print(dict(zip(user_id,first_name)))

# but if we have a three list then we cannot convert it to the dict
# print(dict(zip(user_id,first_name,last_name)))   # error
print(list(zip(user_id,first_name,last_name)))

