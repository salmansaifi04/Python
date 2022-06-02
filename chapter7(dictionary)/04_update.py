user_info = {
    'name' : 'salman',
    'age' : 21,
    'fav_lang' : ['python', 'javascript']
} 

more_data = {
    'name' : 'Salman Saifi', 
    'state' : 'Up'
}

user_info.update({})   # here add empty dictionary
print(user_info)

user_info.update(more_data)
print(user_info)
