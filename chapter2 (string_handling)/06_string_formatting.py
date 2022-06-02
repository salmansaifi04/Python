# string formatting

name = "Salman"
age = 21

print("Hello " + name + " Your age is " + str(age))   # ugly syntax

# python3 string formatting

print("Hello {} your age is {}".format(name, age))
# print("Hello {} your age is {}".format(name, age+2))

# python 3.6 string formatting

print(f"Hello {name} Your age is {age}")
# print(f"Hello {name} Your age is {age+2}")