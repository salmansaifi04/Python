# define a function
# input ---> num , iterable(tuple, list) conatining numbers as a args

# example 
# nums = [1,2,3]
# to_power(3,*nums)

# output ---> [1,8,27]

# if user did't pass any args then give a message 'hey you did't pass args'
# else return list


x = int(input("Enter a number : "))
l = int(input("Enter the size of a list : "))
l1 = []
for i in range(0,l):
    v = int(input("Enter the list item :"))
    l1.append(v)



def to_power(x, *args):
    if args:
        return [i**x for i in args]
    else:
        return "you didn't pass anything"


print(to_power(x,*l1))


