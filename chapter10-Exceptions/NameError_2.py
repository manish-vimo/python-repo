#Since 'Mustafa' is not defined, the following code gives us a 'NameError.'

try:
    name=(Mustafa)
    print(name, 'today is your wedding day')
except NameError:
    print('This code gives a NameError')
    
name=(Mustafa)
print(name, 'today is your wedding day')