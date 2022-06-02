# apply discount 


class Laptop:
    discount = 10
    def __init__(self, brand_name, model_name, price):
        # instance (object) variables
        self.Brand_name = brand_name
        self.Model_name = model_name
        self.Price = price
        self.laptop_name = brand_name + ' ' + model_name

    def apply_discount(self):
        off_price = (Laptop.discount/100)*self.Price
        return self.Price - off_price


# Laptop.discount = 100
l1 = Laptop('Lenovo', 'ideapad', 60000)
l2 = Laptop('apple', 'ipad', 160000)

print(l2.apply_discount())