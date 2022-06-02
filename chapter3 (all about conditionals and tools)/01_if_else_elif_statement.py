# if-else statement 

# age = int(input("Enter your age : "))
# if age >= 14:
#     print("You are above 14")
# else:
#     print("you are not above 14")


# if else elif statement

age = int(input("Enter your age : "))
if age == 0 or age<0:
    print("you can't watch watch")
elif 0<age<=3:
    print("Ticket price : Free")
elif 3<age<=10:
    print("Ticket price : 150")
elif 10<age<=60:
    print("Ticket price : 250")
else:
    print("Ticket price : 200")

# pass statement
x = 18
if x>18:
    pass