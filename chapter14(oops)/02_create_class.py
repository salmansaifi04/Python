# How to create an class
# What is init method (constructure)
# What are attributes, instance variable
# How to create our object

class Person:
    def __init__(self, first_name, last_name, age):
        print("Init method / constructure get called")  # whenever we create the object (p1, p2, p3, ...) this line get print
        # instance (object) variables
        self.First_name = first_name
        self.Last_name = last_name
        self.Age = age


p1 = Person("Salman", "Saifi", 21)
p2 = Person("Prakash", "singh", 21)
p3 = Person("Suraj", "sharma", 21)
print(p1.First_name)
print(p1.Last_name)
print(p1.Age)
