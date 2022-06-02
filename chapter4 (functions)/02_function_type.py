# 1. parameterized function
def add(x,y):
    print(x+y)
add(3,4)

# 2. parameterless function

def sub():
    x = 20
    y = 10
    print(x-y)
sub()

# 3. Default parameter function

def user_info(first_name, last_name = 'unknown', age = None):
    print(first_name)
    print(last_name)
    print(age)

user_info("salman", "saifi")     # no error 
user_info("salman", "saifi", 23) # no error

# 4. positional function
def show(id,name,age,salary):
    print("id", id)
    print("name", name)
    print("age", age)
    print("salary", salary)

show(name= "salman", id = 121, age = 21, salary=50000)

# 5. return type function
# -----------------
def show1(x,y):
    z = x+y 
    return z
t = show1(2,1)
print(t)

# -----------------
def show2(x,y):
    p = 8
    z = x+y 
    return z,p
t1, k = show2(2,1)
print("total : ", t1)
print("p is : ", k)

# -----------------
def show3():
    l = [4,5,6,7,8]
    return l
t2 = list(show3())
print("list is : ",t2)

# -----------------
def show4(k):
    return k
l = [1,22,344,328]
t3 = show4(l)
print(t3)

# 6. recursive function or recursion function :- It is a process to call itself again and again untill the condition satisfy

def facto(x):
    if x == 1:
        return 1
    else:
        return x*facto(x-1)

print(facto(5))
