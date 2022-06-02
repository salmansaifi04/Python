# in keyword in sets and for loop

s = {"a", "b", "c"}

# in keyword to check if item is present or not in set
if "a" in s:
    print("Present")
else:
    print("Not Present")


# for loop
for i in s:
    print(i)

s1 = {1,2,3,4,5,6}
s3 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

## mathmatical operation
# 1. union  (|)   (remove common values)
# print(s1.union(s2))
# print(s1 | s2)

# 2. intersection (&)  (common values)
# print(s1.intersection(s2))
# print(s1 & s2)

## 3. subset()  (it check the all element of s1 is present in s3)
print(s1.issubset(s3))

## 4. superset() (it check the all element of s3 is present in s1) 
print(s1.issuperset(s3))
print(s1)

## 5. Disjoint () (no values match)
print(s1.isdisjoint(s2))
