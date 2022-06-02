from functools import wraps
def only_data_type_allow(datatype):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == datatype for arg in args]):
                return function(*args, **kwargs)
            else:
                return "invalid input"
            # data_types = []
            # for arg in args:
            #     data_types.append(type(arg) == int)
            # if all(data_types):
            #     return function(*args, **kwargs)
            # else:
            #     return "invalid arguments"
        return wrapper
    return decorator


@only_data_type_allow(str)
def string_join(*args):
    string = ''
    for i in args:
        string += i
    return string
print(string_join("salman", "saifi"))