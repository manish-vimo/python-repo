nlis = []
count = 0
try:
    mean = count/len(nlis)
    print('The mean value is', mean)
except ZeroDivisionError:
    print('This code gives a ZeroDivisionError')
    
#Since the variable 'mean' is not defined, it gives us a 'NameError'

#print(mean)