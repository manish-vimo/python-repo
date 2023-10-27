num1 = float(input('Enter a number:'))
print('The entered value is', num1)
try:
    num2 = float(input('Enter a number:'))
    print('The entered value is', num2)
    value = num1/num2
except (ZeroDivisionError, NameError, ValueError): #Multiple except clauses
    print('This function gives a ZeroDivisionError, NameError or ValueError.')
except:
    print('Soething went wrong!')
else:
    print('This process is running with value = ', value)
finally:
    print('The process is completed.')