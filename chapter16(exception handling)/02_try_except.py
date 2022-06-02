## example 1 ##

try:
    x = 10
    y = 0
    z = x/y
    print(z)
except Exception as e:
    print(f"Error is :- {e}")

## **** one try have many except statement but only one is work

## example 2 ##

while True:
    try:
        age = int(input("Enter your age : "))
        break
    except ValueError:
        print('maybe you enter string instead of numbers, try again')
    except:
        print("Invalid input")

if age<18:
    print("You can\'t play this game")
else:
    print("You can play this game")