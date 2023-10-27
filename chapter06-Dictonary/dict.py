# Take a sample dictionary
sample_dict = {'key_1': 3.14, 'key_2': 1.618, 'key_3': True, 'key_4': [3.14, 1.618], 'key_5': (3.14, 1.618), 'key_6': 2022, (3.14, 1.618): 'pi and golden ratio'}
print(sample_dict)

# Accessing to the value using the key
print(sample_dict['key_1'])
print(sample_dict['key_2'])
print(sample_dict['key_3'])
print(sample_dict['key_4'])
print(sample_dict['key_5'])
print(sample_dict['key_6'])
print(sample_dict[(3.14, 1.618)]) # Keys can be any immutable object like tuple