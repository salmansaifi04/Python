# Exercise 1
# ask user's name and age
# if user name start with ('a' or 'A') and age is above 10 then
# print "you can watch movie"
# else "you cannot watch movie"


user_name = input("Enter your name : ")
age = int(input("Enter your age : "))
if (user_name[0] == 'a' or user_name[0] == 'A') and (age >= 10):
    print("You can watch Movie")
else:
    print("You cannot watch movie")