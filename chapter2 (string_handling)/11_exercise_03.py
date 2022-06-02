# take two comma seprated input
# 1.) user's name
# 2.) a single character

# output
# 1.) user's name length
# 2.) count the character that user enter

name, char = input("Enter your name and char of your name using comma seprated : ").split(",")

# print(f"The length of {name} is {len(name)} and {char} is {name.lower().count(char.lower())}")


# using strip method 

print(f"The length of {name} is {len(name.strip())} and {char} is {name.strip().lower().count(char.strip().lower())}")


