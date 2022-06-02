## -------- add and delete data ----------- ##

user_info = {
    'name' : 'salman',
    'age' : 21,
    'fav_lang' : ['python', 'javascript']
} 

## ---- how to add data  ---- ##
user_info['fav_songs'] = ['song1', 'song2']
print(user_info)

## --- add method (set_default---> add at the end) --- ##
user_info.setdefault('id', 111) 
print(user_info)


## ---- pop method ---- ##
popped_item = user_info.pop('fav_songs')
print(type(popped_item))   # it return list (it depend on type of value)
print(f"popped_item is {popped_item}")
print(user_info)

## ---- popitem ---- (it remove random key value pair) ##
popped_item1 = user_info.popitem()
print(f"popped item is {popped_item1}")
print(type(popped_item1))   # it return tuple (it is also depend on type of value)
print(user_info)

