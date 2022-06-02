# practice for loop
# ask user a number like "1234"
# calculate sum of digits ----> 1+2+3+4


num = input("Enter a number like (1234) : ")
total = 0
for i in range(0,len(num)):
    total += int(num[i])
print(total)