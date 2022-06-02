# dictionary comprehension

#### example 1 ####
# squares = {1:1, 2:4, 3:9}

# new_dict = {}
# for i in range(1,11):
#     new_dict.setdefault(i,i**2)
# print(new_dict)


new_dict2  = {i:i**2 for i in range(1,11)}
print(new_dict2)


new_dict3 = {f"Square of {i} is":i**2 for i in range(1,11)}
print(new_dict3)
for k,v in new_dict3.items():
    print(k,v)


### example 2 ### 
name = "Salman Saifi"
# new_dict4 = {}
# for i in name:
#     new_dict4[i] = name.count(i)
# print(new_dict4)
 
word_counter = {i:name.count(i) for i in name}
print(word_counter)


