fruits = ['pear', 'kiwi', 'apple', 'banana']

# for loop
for i in fruits:
    print(i)

# while loop
# j = 0
# while j<len(fruits):
#     print(fruits[j])
#     j+=1


## how to create user define list :-  
x = int(input("Enter the size of a list : "))
l = []
for k in range(0,x):
    y = eval(input('Enter the list item : '))
    l.append(y)

print(l)