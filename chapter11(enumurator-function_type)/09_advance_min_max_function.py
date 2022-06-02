## advance min() and max() function

## ---- example 1 ----
# numbers = [1,5,7,10]
# print(max(numbers))
# print(min(numbers))

## ---- example 2 ----
# names = ["salman", "abc", "xy"]
# print(max(names, key = lambda i:len(i)))
# print(min(names, key = lambda i:len(i)))

## ---- example 3 ----

students1 = [
    {'name':'salman', 'score':90, 'age': 21},
    {'name':'suraj', 'score':60, 'age': 22},
    {'name':'prakash', 'score':70, 'age': 23}
]

# print(max(students1, key = lambda item:item.get('score')).get('name'))
# print(max(students1, key = lambda item:item.get('score'))['name'])

## ----- example 3 -----
students2 = {
    'salman' : {'score':90, 'age':21},
    'prakash' : {'score':50, 'age':22},
    'suraj' : {'score':60, 'age':24}
}

print(max(students2, key=lambda item:students2[item]['age']))
print(max(students2, key=lambda item:students2[item]['score']))

