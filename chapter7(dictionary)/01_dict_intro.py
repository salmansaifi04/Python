## Dictionary :- Dictionaries are used to store data values in key:value pairs.
# It is denoted by {}.
# It is dynamic.
# It store data on key.
# It is collection of object type elements.
# Dictionary key can be any type of data.(int, string)
# Key cannot be null or duplicate.
# It is a unordered collection of data.
# It is a class of collection.


## Q - why we use dictionaries ?
# A - Beacuse of limitations of lists, lists are not enough to represent real data.

## Example
user = ['Salman', [40000], [21]]
# this list contains username, salary, age
# we can do this but this is not good to do this

## Q - What are dictionaries ?
# A - unordered collection of data in 'key : value' pair 


## 1. how to create dictionaries
# user_info = {'first_name' : 'salman', 'last_name' : 'Saifi', 'age' : 21}
# print(user_info)
# print(type(user_info))

# key is 'first_name, last_name, age'   # key are unique
# value is ''salman, saifi, 21'         # but sometime value are same

## 2. Second method to create dictionarie
# user_info1 = dict(name = 'salman', age = 21)
# print(user_info1)

## 3.how access data from dictionary
## Note - There is no indexing beacuse of unordered collection of data
user_info = {'first_name' : 'salman', 'last_name' : 'Saifi', 'age' : 21}

# how to print all keys
print(user_info.keys())

# how to print all values
print(user_info.values())

# how to print items (keys + values)
print(user_info.items())

# how to access value using key
print(user_info['first_name'])


## 4. which type of data a dictionary can store
# It can store anything like numbers, strings, list, dictionary

user_info3 = {
    'name' : 'salman',
    'age' : 21,
    'fav_lang' : ['python', 'javascript']
} 

print(user_info3)
print(user_info3['fav_lang'])

## 5. How to add data to empty dictionary
user_info4 = {}
user_info4['name'] = 'salman'
print(user_info4)