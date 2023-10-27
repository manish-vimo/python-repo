# Take a nested tuple
nested_tuple =('biotechnology', (0, 5), ('fermentation', 'ethanol'), (3.14, 'pi', (1.618, 'golden ratio')) )
print(nested_tuple)

# Now printing the each element of the nested tuple
print('Item 0 of nested tuple is', nested_tuple[0])
print('Item 1 of nested tuple is', nested_tuple[1])
print('Item 2 of nested tuple is', nested_tuple[2])
print('Item 3 of nested tuple is', nested_tuple[3])

print()

# Using second index to access other tuples in the nested tuple
print('Item 1, 0 of the nested tuple is', nested_tuple[1][0])
print('Item 1, 1 of the nested tuple is', nested_tuple[1][1])
print('Item 2, 0 of the nested tuple is', nested_tuple[2][0])
print('Item 2, 1 of the nested tuple is', nested_tuple[2][1])
print('Item 3, 0 of the nested tuple is', nested_tuple[3][0])
print('Item 3, 1 of the nested tuple is', nested_tuple[3][1])
print('Item 3, 2 of the nested tuple is', nested_tuple[3][2])

print()

# Accesing to the items in the second nested tuples using a third index
print('Item 3, 2, 0 of the nested tuple is', nested_tuple[3][2][0])
print('Item 3, 2, 1 of the nested tuple is', nested_tuple[3][2][1])