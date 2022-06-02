## raise :- It is useful to throw a user define exception.

## Example 1 ##
# def show(x):
#     if x>15000:
#         raise Exception ("You can't withdraw")
#     else:
#         print("success")

# show(18000)

## Example 2 ##

def show2(x,y):
    if y==2:
        raise Exception("You cannot divide by 2")
    else:
        z = x/y
        print(z)

show2(2,2)