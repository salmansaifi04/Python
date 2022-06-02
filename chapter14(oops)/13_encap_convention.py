# Encapsulation
# Some special naming convention
# _name ---> convention for private name
# __name__ ---> dunder\magic methods

# Name mangling , __name (this is not a convention)

class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self._model_name = model_name
        self.__price = price

    def make_a_call(self, number):
        print(f"Calling {number} ...")
    
    def full_name(self):
        return f"{self.brand} {self.model_name}"

# phone1 = Phone('nokia', 1100, 3000)

### *** __name ***
# print(phone1.__price)    # error because python change the name of phone1.__price to phone1._Phone__price
# print(phone1.__dict__)
# print(phone1._Phone__price)
# phone1._Phone__price = 100
# print(phone1._Phone__price)


### **** _name ****
# print(phone1._model_name)
# phone1._model_name = 200
# print(phone1._model_name)

