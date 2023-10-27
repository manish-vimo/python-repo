tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3}, {'A': 3, 'B': 8}, (0, 1))
print(tuple_1)

print(type(tuple_1))
print(len(tuple_1))

print()

# Printing the each value in a tuple using both positive and negative indexing
print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[2])
print(tuple_1[-1])
print(tuple_1[-2])
print(tuple_1[-3])
print(tuple_1[-4])

print()

# Printing the type of each value in the tuple
print(type(tuple_1[0]))
print(type(tuple_1[2]))
print(type(tuple_1[4]))
print(type(tuple_1[6]))
print(type(tuple_1[7]))
print(type(tuple_1[8]))
print(type(tuple_1[9]))
print(type(tuple_1[10]))


#Concatenation of tuples // To concatenate tuples, + sign is used

tuple_2 = tuple_1 + ('Hello World!', 2022)
print(tuple_2)