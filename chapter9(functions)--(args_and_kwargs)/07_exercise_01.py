def func(l, **kwargs):
    if kwargs.get('reverse_str') == True:
        return [i[::-1].title() for i in l]
    else:
        return [i.title() for i in l]


print(func(["salman", "saifi"]))
print(func(["salman", "saifi"], reverse_str = True))