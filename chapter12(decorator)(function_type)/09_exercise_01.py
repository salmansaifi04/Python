# how to calculate time
from functools import wraps
import time
# t1 = time.time()
# print("This is line 1")
# x = 5
# if x == 5:
#     print("x is equal to 5")
# print("This is line 2")
# t2 = time.time()
# print(t2-t1)


def cal_time(any_function):
    @wraps(any_function)
    def inner_func(*args, **kwargs):
        t3 = time.time()
        returned_value = any_function(*args, **kwargs)
        t4 = time.time()
        print(t4-t3)
        return returned_value
    return inner_func

@cal_time
def square(n):
    return [i**2 for i in range(1,n+1)]

square(100000)
