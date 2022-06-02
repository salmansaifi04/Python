### list ###
fruits = ['grapes', 'mango', 'apple']
## sort method
# fruits.sort()
# print(fruits)


### tuple ###
fruits2 = ('grapes', 'mango', 'apple')
## but we don't have a sort method in tuple because tuple is immutable
# fruits2.sort()   # it gives error

## but we can use sorted function (it create a list)
# print(sorted(fruits2))


### sets (sets have no order) ###
fruits3 = {'grapes', 'mango', 'apple'}
print(sorted(fruits3))


#### advance example ####

guitars = [
    {'model':'yamaha f310', 'price':8400},
    {'model':'faith naptune', 'price':50000},
    {'model':'faith apollo venus', 'price':35000},
    {'model':'taylor 814ce', 'price':450000}
]


print(sorted(guitars, key= lambda d:d['price']))
print(sorted(guitars, key= lambda d:d['price'], reverse=True))



