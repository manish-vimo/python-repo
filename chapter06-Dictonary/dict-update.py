#update() function
#It integrates a dictionary with another dictionary or with an iterable of key:value pairs.

product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
'Aspergillus sojae_2': 'polygalacturonase'}

sample_original = dict(family = 'music', type='pop', year='2022' , name='happy new year')

product.update(sample_original)
print(product)

#items() function
#It returns a list of key:value pairs in a dictionary. The elements in the lists are tuples.
print(product.items())

#Iterating dictionary
#A dictionary can be iterated using the for loop
print()
for k in product:
    print(k)
    
print()
print("TO print values by value function():")
# 'for' loop to print the values of the dictionary by using values() and other method
for x in product.values():
    print(x)

print()    
print("To print values:")
# 'for' loop to print the values of the dictionary by using values() and other method
for x in product:
    print(product[x])

print()    
print("To print x & y:")    
for x, y in product.items():
    print(x, y)