# firstly we have understand the function in details
# then closures

def square(num):
    return num**2

# s = square(7)
# print(s)

# s and square are same because we assign the sqaure in s
s = square
print(s(7))

print(s.__name__)
print(square.__name__)

print(s)
print(square)