# define a function that take list as a argument 
# return a reversed list


# using reverse method
def reverse_list(l):
    l.reverse()
    return l

l = [1,2,3]
print(reverse_list(l))


# using string slicing [::-1]
def reverse_list1(l):
    return l[::-1]
l2 = [1,2,3]
print(reverse_list1(l))

# using append and pop method
def reverse_list2(l):
    r_list = []
    for i in range(len(l3)):
        popped_item = l3.pop()
        r_list.append(popped_item)
    return r_list

l3 = [1,2,3,4]
print(reverse_list2(l3))