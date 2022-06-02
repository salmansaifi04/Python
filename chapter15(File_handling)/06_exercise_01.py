## Salman's salary is 50000
## Prakash's salary is 5 
## Suraj's salary is 5 

with open("01_demo.txt", "r") as rf:
    with open("output01.txt", "a") as af:
        for line in rf.readlines():
            name, salary = line.split(",")
            af.write(f"{name}\'s salary is {salary}")