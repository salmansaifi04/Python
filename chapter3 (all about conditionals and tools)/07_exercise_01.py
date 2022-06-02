# sum of n natural numbers
# ask a user for n natural number
# print total from 1 to n

total = 0
i = 1
num = int(input("Enter a number : "))
while i<=num:
    total += i
    i += 1
print(f"The sum of number between 1 to {num} is {total}")