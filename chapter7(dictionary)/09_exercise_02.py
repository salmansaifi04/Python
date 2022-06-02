# ouput --->
# user = {
    # 'name' : 'salman',
    # 'age' : 21,
    # 'fav_song' : ['song1', 'song2] 
# }


user = {}
name = input("Enter your name : ")
age = int(input("Enter your age : "))
fav_song = input("Enter your fav_song comma seprated").split(",")

user['name'] = name
user['age'] = age
user['fav_song'] = fav_song

print(user)

for key, value in user.items():
    print(f"{key} : {value}")