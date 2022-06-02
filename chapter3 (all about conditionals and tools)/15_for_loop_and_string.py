# for loop and string

# all programming language
name = "Salman"
for i in range(len(name)):
    print(name[i])

# In python
for j in name:
    print(j)

# 1234 ----> 1+2+3+4

num = input("Enter a number like (1234) : ")
total = 0
# new method 
for i in num:
    total += int(i)
print(total)

## old method
# for i in range(0,len(num)):
#     total += int(num[i])
# print(total)
