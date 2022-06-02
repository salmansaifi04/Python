# class variable or class attribute

class Circle:
    pi = 3.14
    def __init__(self,r):
        self.r = r 
    def calc_circumference(self):
        return 2*Circle.pi*self.r

c = Circle(10)
print(c.calc_circumference())