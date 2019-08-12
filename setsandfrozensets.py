#***********SETS AND FROZENSETS*******
# x = frozenset([2,4,7,23,4])
# y = set([2,4,5])
# z = {2,6,7,8,9,10,11,12}
# print(x)
# print(y)
# union = x.union(y)
# print(union)
y = set([2,4,5,6])
z = {2,6,7,8,9,10,11,12}
x = {2,4,5}
print(y | z)
print(y & z)
print(y - z) 
print(y ^ z) #symmetric difference common elements ko hata kr baqi sary 
print(y > z) # a superset
print(y < z) #a subset
print(x < y) # x is a subset of y
print(x > y) # x is not a superset
print(y < x)
print(y > x)
print(y.intersection(z))
print(y.union(z))
print(y.difference(z))
print(y.issubset(x))
print(y.issuperset(x))