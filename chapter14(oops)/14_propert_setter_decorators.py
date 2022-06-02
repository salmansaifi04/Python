class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)
        # if price>0:
        #     self.price = price
        # else:
        #     self.price = 0
        # self.complete_specification = f"{self.brand} {self.model_name}, {self.price}"

    @property
    def complete_specification(self):
        return f"{self.brand} {self.model_name}, {self._price}"


    # getter , setter

    @property       # getter method 
    def price(self):
        return self._price

    @price.setter   # setter method
    def price(self, new_price):
        self._price = max(new_price, 0)



    def make_a_call(self, number):
        return f"Calling to {number}"
    
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self.price}"


phone1 = Phone('Nokia', 1100, 2000)
phone1.price = -500
# phone1.price = 500
print(phone1.price)
# print(phone1.complete_specification())  # without propert decorator
print(phone1.complete_specification)    # with propert decorator
