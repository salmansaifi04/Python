# user define dictionary

x = int(input("Enter the size pf a dictionary : "))
d = {}
for i in range(0,x):
    k = eval(input("Enter the key : "))
    v = eval(input("Enter the Value : "))
    d.setdefault(k,v)
print(d)