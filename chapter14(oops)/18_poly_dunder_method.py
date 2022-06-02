class Phone:  # base class / parent class
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self._price = max(price, 0)
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

    # str, repr
    def __str__(self):
        return f"{self.model_name} {self.brand} and price is {self._price}"
        
    # it is for developer 
    def __repr__(self):
        return f"Phone(\'{self.model_name}\', \'{self.brand}\', \'{self._price}\')"

    # len function
    def __len__(self):
        return len(self.full_name())

    # operator overloading
    def __add__(self, other):
        return self._price + other._price



phone = Phone('Nokia', '1100', 1000)
phone1 = Phone('Nokia', '1300', 1200)
print(phone)   # with the help of __str__, __repr__  
print(repr(phone))   # with the help of __str__, __repr__  
print(phone.__repr__())   
print(phone.__len__())
print(phone + phone1)   # opertaor overloading



class Smartphone(Phone):     # derived class / child class
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        # two ways
        # Phone.__init__(self, brand, model_name, price)   # uncommon way
        super().__init__(brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

