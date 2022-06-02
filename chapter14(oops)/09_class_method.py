# class methods
# difference between class method and instance (object) method

class Person:
    count_instance = 0     # class variable or class attribute

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    @classmethod
    def count_instances(cls):  # class method
        return f"You have created {cls.count_instance} object of your {cls.__name__} class"

    def full_name(self):    # instance (object) method
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):  # instance (object) method
        return self.age>18

p1 =  Person("Salman","Saifi", 21)
p2 =  Person("Salman","Saifi", 21)

print(Person.count_instances())