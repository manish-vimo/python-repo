num1 = float(input('Enter a number:'))
print('The entered value is', num1)
try:
    num2 = float(input('Enter a number:'))
    print('The entered value is', num2)
    value = num1/num2
except ZeroDivisionError:
    print('This function gives a ZeroDivisionError since a number cannot divide by 0.')
except ValueError:
    print('You should provide a number.')
except:
    print('Something went wrong!')
else:
    print('This process is running with value = ', value)