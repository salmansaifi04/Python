###### function practice ######

# 1. return last charcter
def last_char(s):
    return s[-1]
print(last_char("salman"))

# 2. odd even function

# def odd_even(n):
#     if n%2 == 0:
#         return f"{n} is even"
#     else:
#         return f"{n} is odd"

def odd_even(n):
    if n%2 == 0:
        return f"{n} is even"
    return f"{n} is odd"

print(odd_even(5))
print(odd_even(2))

# 3. is_even function

def is_even(n):
    return n%2 == 0
print(is_even(10))
print(is_even(1))



# parameter and argument
# in above example
# n is a parameter
# 10, 1 is a argument 