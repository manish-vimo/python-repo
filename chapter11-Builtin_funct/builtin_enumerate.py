str_list = ['Hello Python!','Hello, World!']
for i, str_list in enumerate(str_list):
    print(i, str_list)
    
print()

str_list = ['Hello Python!','Hello, World!']
enumerate_list = enumerate(str_list)
print(list(enumerate_list))