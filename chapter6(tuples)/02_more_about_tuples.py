mixed = (1,'two',3.0,'four',None)

## 1. looping in tuples
# for loop :-
for i in mixed:
    print(i)

# while loop :-
j = 0
while j<len(mixed):
    print(mixed[j])
    j+=1


## 2. tuple with one elements

t1 = (1)   # its int
t2 = (1,) # its tuple
word = ('word1') # its str
word1 = ('word1',) # its tuple

print(type(t2))
print(type(t1))
print(type(word))
print(type(word1))


## 3. tuple with parenthesis

words = 'one', 2, 'three', 4.0, None    # its tuple
print(type(words))


## 4. tuple unpacking
guitars = 'yahama', 'baton rouge', 'taylor'
guitar1, guitar2, guitar3 = guitars
print(guitar1)
print(guitar2)
print(guitar3)


## 5. list inside tuple
t = (1,['two', 3, 'four', None])
t[1].pop()
# t[1].append("'five")
# t[1].insert(2,"'five")

print(t)

## 6. some functions that you can use with tuples
# 1. min()
# 1. max()
# 1. sum()
number = (2,10,11,70,21)
print(min(number))
print(max(number))
print(sum(number))

