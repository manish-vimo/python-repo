dictionary = {'euler_constant':0.577, 'golden_ratio':1.618}
try:
    dictionary = dictionary['euler_number']
except KeyError:
    print('This code gives us a KeyError')
    
dictionary = dictionary['euler_number']
print(dictionary)