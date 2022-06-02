# set comprehension 

s = {i**2 for i in range(1,11)}
print(s)

names = ['Salman', "Prakash", "Suraj"]
s1 = {i[0] for i in names}
print(s1)