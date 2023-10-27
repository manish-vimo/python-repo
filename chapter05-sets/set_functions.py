# Addition of an element to a set
set3 = set(['Hello Python!', 3.14, 1.618, 'Hello World!', 3.14, 1.618, True, False, 2022])
set3.add('Hi, Python!')
print(set3)

# Addition of the same element
set3.add('Hi, Python!')
set3
# As you see that there is only one from the added element 'Hi, Python!'

#update() function
#To add multiple elements into the set

x_set = {6,7,8,9}
print(x_set)
x_set.update({3,4,5})
print(x_set)


#remove() function
#To remove an element from the set

set3.remove('Hello Python!')
print(set3)


#discard() function
#It leaves the set unchanged if the element to be deleted is not available in the set.

set3.discard(3.14)
print(set3)

# To verify if the element is in the set
print(1.618 in set3)