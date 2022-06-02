# define a function that take list as a input 
# and the print square of a every element



def square_value(l):
    output = [] 
    for i in l:
        output.append(i**2)
    print(output)

square_value(range(1,11))