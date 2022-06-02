# ask a user name 
# Example - "salman saifi"
# print  "count of each word"
# for example 
# s:2
# a:3
# l:1
# m:1
# n:1
#  :1
# i:2
# f:1


user_name = input("Enter your name : ")
temp = ""
for i in range(len(user_name)):
    if user_name[i] not in temp:
        temp += user_name[i]
        print(f"{user_name[i]} : {user_name.count(user_name[i])}")
