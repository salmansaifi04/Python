## w, a, r+, copy from the one file and paste it to the another file

## "w" mode overwrite the code and if file is not present it create it automatically
# with open("demo1.txt", "w") as f:
#     f.write("Hello")


## "a" mode append the text after the words and if file is not present it create it automatically 
# with open("demo2.txt", "a") as f:
#     f.write("My name is Salman")


## "r+" mode only read and write if file is already create and it write the text at the starting
# with open("demo1.txt", "r+") as f:
#     f.seek(len(f.read()))
#     f.write("abc")

## copy from the one file and paste it to the another file

# with open("demo1.txt", "r") as rf:
#     with open("demo2.txt", "w") as wf:
#         wf.write(rf.read())