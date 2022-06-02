# multilevel inheritance

class Phone:  # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)

    def make_a_call(self, number):
        return f"Calling to {number}"
    
    def full_name(self):
        return f"{self.brand} {self.model_name} and price is {self._price}"


class Smartphone(Phone):     # derived class / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)   # uncommon way
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera


class FlagshipPhone(Smartphone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model_name, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera



# phone = Phone('Nokia', '1100', 1000)
smartphone = Smartphone('samsung', 'j7', 15000, '4GB', '64GB', '8mp')
smartphone2 = FlagshipPhone('samsung', 'j7', 15000, '4GB', '64GB', '8mp','16px')
# print(smartphone.full_name())
# print(smartphone2.front_camera)


## ----- method resolution order ----- ##
# print(help(Smartphone))
# print(help(FlagshipPhone))
# print(Smartphone.mro())
# print(Smartphopne.__mro__)

## ----- isinstance(), issubclass() ----- ##

print(isinstance(smartphone, Smartphone))
print(isinstance(smartphone, Phone))

print(issubclass(Smartphone, Phone))
print(issubclass(Smartphone, FlagshipPhone))