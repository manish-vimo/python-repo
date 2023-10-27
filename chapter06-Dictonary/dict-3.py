# Take a sample dictionary
product = {'Aspergillus niger': 'inulinase', 'Saccharomyces cerevisiae': 'ethanol',
'Scheffersomyces stipitis': 'ethanol', 'Aspergillus sojae_1': 'mannanase',
'Streptococcus zooepidemicus': 'hyaluronic acid', 'Aspergillus sojae_2': 'polygalacturonase'}

#check existance
print('Saccharomyces cerevisiae' in product)
print('Saccharomyces cerevisiae' not in product)

#clear() function
#It removes all the items in the dictionary and returns an empty dictionary
dict_sample = dict(family = 'music', type='pop', year='2022' , name='happy new year')
dict_sample.clear()
print(dict_sample)