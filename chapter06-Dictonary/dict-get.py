# get() function
#This method returns the value for the specified key if it is available in the dictionary. If the key is not available, it returns None.

sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')
print(sample_original.get('family'))
print(sample_original.get('year'))
print(sample_original.get('33'))