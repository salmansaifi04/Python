## --------- in keyword and iterations ---------

user_info = {
    'name' : 'salman',
    'age' : 21,
    'fav_lang' : ['python', 'javascript']
} 

## ------- check if key exist in dictionary ---------
# if 'name' in user_info:
#     print('present')
# else:
#     print('not present')

# if 'name' in user_info.keys():
#     print('present')
# else:
#     print('not present')


## --------- check if value exist in dictionary -----------
## above code give error
'''if 'name' in user_info:
    print('present')
else:
    print('not present')
    '''
## above code is error free
# if 'salman' in user_info.values():
#     print('present')
# else:
#     print('not present')

## how to list
# if  ['python', 'javascript'] in user_info.values():
#     print('present')
# else:
#     print('not present')


## ------ loops in dictionary -----
## print all keys
for i in user_info:
    print(i)

## print all values
for i in user_info.values():
    print(i)

## print keys and values or items
for i in user_info.items():
    print(i)

## ------ ##
for key, value in user_info.items():
    print(f"key is {key} and value is {value}")
