# in keyword with if

from doctest import Example


name = "salman"
if 'a' in name:
    print("a is present")
else:
    print("Not present")


# check empty or not

string = "string"
if string:
    print("String is not empty")
else:
    print("String is empty")

# Example

user_name = input("Enter your name : ")
if user_name:
    print(f"Your name is {user_name}")
else:
    print("You didn't type anything")