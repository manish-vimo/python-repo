#Identity operators
#The operators is or is not are employed to control if the operands or objects to the left and right of these
#operators are referring to a value stored in the same momory location and return True or False.

a = 3.14
b = 1.618
print(a is b)
print(a is not b)

print()

msg1= 'Hello, Python!'
msg2 = 'Hello, World!'
print(msg1 is msg2)
print(msg1 is not msg2)

print()

lis1 = [3.14, 1.618]
lis2 = [3.14, 1.618]
print(lis1 is lis2) # You should see a list copy behavior
print(lis1 is not lis2)