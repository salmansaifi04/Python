# any all function practice

def all_sum(*args):
    total = 0
    for i in args:
        total += i
    return total

# print(all_sum(1,2,3,4))    # correct input
# print(all_sum(1,2,3,4, "salman", ["salman"]))    # wrong input


## here we solve the problem of wrong input using all function
def all_add(*args):
    if all([(type(arg) == int or type(arg) == float) for arg in args]):
        total = 0
        for i in args:
            total += i
        return total
    else:
        return "wrong input"



print(all_add(1,2,3,4))   
print(all_add(1,2,3,4, "salman", ["salman"]))   

