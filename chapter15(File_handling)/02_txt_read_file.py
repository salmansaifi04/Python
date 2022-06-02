## readfile
## open function
## read method
## seek method   ---> change cursor position
## tell method   ---> print cursor position
## readline method
## readlines method 
## close method

f = open("01_demo.txt", "r")
print(f.read())
# print(f.tell())
# print(f.readline())
# print(f.readlines())
# f.seek(0)
# print(f.readlines())

## name, closed
# print(f.name)
# print(f.closed)

f.close()