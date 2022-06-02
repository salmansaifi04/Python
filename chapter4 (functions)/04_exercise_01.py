# define function which takes two numbers as a input and return greater of two number

def greater_num(n1,n2):
    if n1>n2:
        return f"{n1} is greater than {n2}"
    else:
        return f"{n2} is greater than {n1}"

# num1 = int(input("Enter a first number : "))
# num2 = int(input("Enter a second number : "))
# print(greater_num(num1, num2))


# define function which takes three numbers as a input and return greater of three number

def greatest_num(n1,n2,n3):
    if n3<n1>n2:
        return f"{n1} is greater"
    elif n3<n2>n1:
        return f"{n2} is greater"
    else:
        return f"{n3} is greater"

n1 = int(input("Enter a first number : "))
n2 = int(input("Enter a second number : "))
n3 = int(input("Enter a third number : "))
print(greatest_num(n1,n2,n3))