## instance method or object method

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    def full_name(self):   # instance (object) method
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):  # instance (object) method
        return self.age>18

p1 =  Person("Salman","Saifi", 21)
print(p1.full_name())    # as below print statement
# another way to print full name 
print(Person.full_name(p1))   # as above print statement

print(p1.is_above_18())