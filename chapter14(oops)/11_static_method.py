# class method as a constructor

class Person:
    count_instance = 0     # class variable or class attribute

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 

    @classmethod
    def from_string(cls, string):
        first, last, age = string.split(",")
        return cls(first, last, age)

    @classmethod
    def count_instances(cls):  # class method
        return f"You have created {cls.count_instance} object of your {cls.__name__} class"

    @staticmethod
    def hello():
        print("hello, static method call")


    def full_name(self):    # instance (object) method
        return f"{self.first_name} {self.last_name}"

    def is_above_18(self):  # instance (object) method
        return self.age>18

p1 =  Person("Salman","Saifi", 21)
p2 =  Person("Salman","Saifi", 21)

p3 = Person.from_string("salman,saifi,21")
p3.hello()