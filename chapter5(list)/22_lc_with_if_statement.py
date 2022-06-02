# list comprehension with if statement


# even_nums = []
# for i in range(1,11):
#     if i%2 == 0:
#         even_nums.append(i)
# print(even_nums)

# list comprehension
even_nums1 = [i for i in range(1,11) if i%2 == 0]
print(even_nums1)

odd_nums = [i for i in range(1,11) if i%2 != 0]
print(odd_nums)