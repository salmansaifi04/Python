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


name = input("Enter your name : ")
temp = ""
i = 0
while i<len(name):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1