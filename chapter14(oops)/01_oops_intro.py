## oops (object oriented programming system) :- It is a methology and techinique to develop a real world programming implementation.
# It provide a secure programming.
# It provides a dynamic programming.
# It provide a structure programming.
# It provide a object programming.


## ----- Oops elements ----- ##
# 1. Class
# 2. Method 
# 3. Object
# 4. Attributes

## 1. Class :- Class is a blueprint and prototype. We can declare all datamember or member function inside a class. Class provide a structue of your programming.

## 2. Method :- Method is a members of your class which is declare inside in a class. Method are useful to perform any logic and instruction in your code. 

## 3. Object :- It is a current instatnce of your class. It is a reak world entity of your class. It allocate a dynamic memory.

## 4. Attributes :- It is a member of your class which is declare inside in a class and outside of the method. It is also known as datamembers.

## ---- self keyword ---- ##
## self :- self is a keyword to return a current instance of your class. It represent the our object. 



### ---- basic example ---- ###
class One:   # class name 'One'
    x = 10   # class variable or attribute
    y = 20   # class variable or attribute
    def add(self):    # class method not function
        t = self.x + self.y 
        print(t)


k = One()     # 'k' is class instance, 'One()' is class object, 
k.add() 


### ----- constructor or __init__ method ----- ###
# Constructor is denoted by __init__()
# It is useful to allocate a dynamic memory of your class.
# It is useful to create a instance member of your class or allocate memory of instance member of your class.

## --- We have a two type of constructor --- ##
# 1. parameterized constructor 
# 2. parameterless constructor

# 1. parameterized constructor :- 

class Emp:
    def __init__(self, id, first_name, last_name, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def show(self):
        print("Id is", self.id)  
        print("First_name is", self.first_name)  
        print("Last_name is", self.last_name)  
        print("Age is", self.age)  

emp1 = Emp(111, "Salman", "Saifi", 21)
emp1.show()


# 2. parameterless constructor :-
class Emp2:
    def __init__(self):
        self.id = 112
        self.first_name = "Salman"
        self.last_name = "Saifi"
        self.age = 21

    def show(self):
        print("id is", self.id)
        print("first_name is", self.first_name)
        print("last_name is", self.last_name)
        print("age is", self.age)

emp2 = Emp2()
emp2.show()