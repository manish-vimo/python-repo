# Take a sample dictionary
product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
'Streptococcus zooepidemicus': 'hyaluronic acid', 'Lactobacillus casei': 'lactic acid',
'Aspergillus sojae_2': 'polygalacturonase'}

#access values by keys
print(product['Aspergillus niger'])
print(product['Saccharomyces cerevisiae'])
print(product['Scheffersomyces stipitis'])

# print all keys
print(product.keys())

#print all values
print(product.values())

#Addition of a new key:value pair in the dictionary
product['Yarrovia lipolytica'] = 'microbial oil'

print(product)

#Delete an item using del() function in the dictionary by key
del(product['Aspergillus sojae_1'])
del(product['Streptococcus zooepidemicus'])

print(product)

del product
print(product)
# The dictionary was deleted.