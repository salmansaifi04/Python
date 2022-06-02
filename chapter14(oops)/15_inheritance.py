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


k = Smartphone('samsung', 'j7', 15000, '4GB', '64GB', '8mp')
print(k.brand)
print(k.model_name)
print(k.internal_memory)
print(k.ram)
print(k._price)
print(k.rear_camera)