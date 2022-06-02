## how to dlt file 

# import os
# os.remove("demo1.txt") 

## how to check file exist or not

# import pathlib
# s = pathlib.Path("01_demo.txt")

# if s.exists():
#     print("present")
# else:
#     print("Not present")

## how to create // remove folder
# import os 
# os.mkdir("d:/ddd")   # create 
# os.rmdir("d:/ddd")   # remove // delete

## How to search word from the file 

# with open("demo1.txt") as f:
#     s = f.read()
#     print(s)

# x = input("Enter the search word : ")
# if x in s:
#     print(f"{x} is present")    
# else:
#     print(f"{x} is not present")    

## how to get all file list from any drive 
# import os
# s = os.listdir("d://")
# for i in s:
#     print(i)