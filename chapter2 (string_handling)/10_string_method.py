# string method 

name = "sAlmAn SaiFI"

# 1. len() function
print(len(name))

# 2 . lower() method
print(name.lower())

# 3. upper() method
print(name.upper())

# 4. title() method 
print(name.title())

# 5. count() method
print(name.count("a"))

# 6. capitilize() method 
print(name.capitalize())

# 7. swapcase() method 
print(name.swapcase())

# 8. casefold() method  (convert to lower case) 
print(name.casefold())

# 9. encode() method 
print(name.encode())

# 10. index() method 
print("salman".index("a"))

# 11. join() method 
myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)

# 12. strip() method 
name = "      salman          "
dots = "..............."
full = name + dots
print(full)
print(full.lstrip())
print(name.rstrip()+ dots)
print(name.strip())

# 13. replace() method 
print(full.replace(" ",""))
string = "she is beautiful and she is good dancer"
print(string.replace("is", "was"))
print(string.replace("is", "was", 1))


# 14. center() method 
print("salman".center(12, "*") )


# 15. find() method 
# print(string.find("is"))
temp = string.find("is")
print(string.find("is", temp+1))