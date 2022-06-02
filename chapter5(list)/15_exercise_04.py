# filter odd/even 
# define a function
# input   -----> [1,2,3,4,5,6,7]

# output ------> [[1,3,5,7],[2,4,6]]

def odd_even(l):
    odd_values = []
    even_values = []
    for i in l:
        if i%2 == 0:
            even_values.append(i)
        else:
            odd_values.append(i)
    output = [odd_values , even_values]
    return output


l =  [1,2,3,4,5,6,7]
print(odd_even(l))