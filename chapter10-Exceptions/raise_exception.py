num = int(input('Enter a number:'))
print('The entered value is', num)
try:
    if num>1000 and num %2 == 0 or num %2 !=0:
        raise Exception('Do not allow to the even numbers higher than 1000.')
except:
    print('Even or odd numbers higher than 1000 are not allowed!')
else:
    print('This process is running with value = ', num)
finally:
    print('The process is completed.')