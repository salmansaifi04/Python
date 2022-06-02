######### string indexing #########
lang = "python"

# positions

# p ---> 0   ---->  -6
# y ---> 1   ---->  -5
# t ---> 2   ---->  -4
# h ---> 3   ---->  -3
# o ---> 4   ---->  -2
# n ---> 5   ---->  -1


print(lang[2])
print(lang[-1])


######### string slicing ############

# syntax - [start argument : stop argument -1]

print(lang[0:3])    # output = pyt

print(lang[0:])     # output = python

print(lang[:4])     # output = pyth

print(lang[:])      # output = python

print(lang[-3:6])   # output = hon


########### step argument ############

# syntax - [start argument : stop argument -1 : step argument]
print(lang[0:5:1])    # output = pytho
print(lang[0:5:2])    # output = pto
print(lang[::3])    # output = ph
print(lang[::-1])    # output = nohtyp


