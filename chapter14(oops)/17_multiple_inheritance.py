# multiple inheritance

class A:
    def class_a_method(self):
        return 'I\'m just a class A method'

    def hello(self):
        return 'hello from class A'



class B:
    def class_b_method(self):
        return 'I\'m just a class B method'

    def hello(self):
        return 'hello from class B'


class C(A,B):
    pass

k = C()
print(k.class_a_method())
print(k.class_b_method())
print(k.hello())