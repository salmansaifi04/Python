# exercise 
# ask user to input a number containing more than one digit
# example 1234
# calculate 1+2+3+4



num = input("Enter the number for example (1234) : ")

i = 0
total = 0
while i<len(num):
    total += int(num[i])
    i+=1

print(total)