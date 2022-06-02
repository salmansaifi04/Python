## function returning function (closures) practice

## how to define a one function which is useful for cube, sqaure etc


def to_power(pow):
    def calc_power(num):
        return num**pow
    return calc_power

# finding the cube
cube = to_power(3)
print(cube(8))

# finding the square
square = to_power(2)
print(square(3))

