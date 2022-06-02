# scope

##### first case #####
# def func():
#     x = 7   # local variable
#     print(x)

# # func()       # no error
# # print(x)     # gives error


##### second case #####
# x = 10      # global variable
# def func():
#     x = 7   # local variable
#     print(x)

# func()       # no error
# print(x)     # no error
'''in this case x value cannot be change'''

##### third case #######
x = 10      # global variable
def func():
    global x
    x = 7   # local variable
    print(x)
    
print(x)
func()       # no error
print(x)     # no error
'''in this case x value change'''