#### strings :- 
# It is a collection of character inside single quote or double quote
# It is immutable


first_name = "Salman"
last_name = "Saifi"
full_name = first_name + " " + last_name
print(full_name)

# we cannot add string to integer
# print(first_name + 3)    # it gives type error

# but
print(full_name + "3")
print(full_name + str(3))

# we can use multiply sign 
print("hello"*3)