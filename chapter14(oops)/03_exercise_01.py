# Create a laptop class with attributes like brand name, model name, price
#  create two objects/instance of your laptop class

class Laptop:
    def __init__(self, brand_name, model_name, price):
        # instance (object) variables
        self.Brand_name = brand_name
        self.Model_name = model_name
        self.Price = price
        self.laptop_name = brand_name + ' ' + model_name


l1 = Laptop('Lenovo', 'ideapad', 60000)
print(l1.laptop_name)
l2 = Laptop('apple', 'ipad', 160000)