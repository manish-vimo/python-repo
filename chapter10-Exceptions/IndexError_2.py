#You can also supplytake this error type with tuple
tuple_sample = (0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729)
try:
    tuple_sample[10]
except IndexError:
    print('This code gives us a IndexError.')
    
print(tuple_sample[10])