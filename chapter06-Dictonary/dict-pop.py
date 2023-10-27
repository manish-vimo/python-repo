#pop() function
#This function is used to remove a specific item from the dictionary

sample_original = dict(family = 'music', type='pop1', year='2022' , name='happy new year')
print(sample_original.pop('type'))
print(sample_original)

#popitem() function
#It is used to remove the abitrary items from the dictionary and returns as a tuple.
#TypeError: popitem() takes no arguments (1 given)

sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')
print(sample_original.popitem(type))
print(sample_original)