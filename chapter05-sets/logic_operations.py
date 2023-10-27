# Take two sets
set4 = set(['Hello Python!', 3.14, 1.618, 'Hello World!'])
set5 = set([3.14, 1.618, True, False, 2022])
# Printing two sets
print(set4, set5)


#To find the intersect of two sets using &
intersection = set4 & set5
print(intersection)

#To find the intersect of two sets, use intersection() function
print(set4.intersection(set5)) # The output is the same as that of above

#difference() function - To find the difference between two sets
print(set4.difference(set5))
print(set5.difference(set4))

# The same process can make using subtraction operator as follows:
print(set4-set5)
print(set5-set4)


#Set comparison
print(set4>set5)
print(set5>set4)
print(set4==set5)

#union() function - it corresponds to all the elements in both sets
print(set4.union(set5))


#issuperset() and issubset() functions
#To control if a set is a superset or a subset of another set
print(set(set4).issuperset(set5))
print(set(set4).issubset(set5))

print()

print(set([3.14, 1.618]).issubset(set5))
print(set([3.14, 1.618]).issubset(set4))
print(set4.issuperset([3.14, 1.618]))
print(set5.issuperset([3.14, 1.618]))