#Retturns True if all elements in passes iterable are true. When the iterable object is empty, it returns True. Here, 0 and False return False in this function.
nlis1 = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(all(nlis1))
nlis1.append(0) # Add '0' to the end of the list
print(nlis1)
print(all(nlis1))
print("*********")
nlis1.append(False) # Adds 'False' to the end of the list
print(nlis1)
print(all(nlis1))
print("*********")
nlis1.clear() # It returns an emtpy list
print(nlis1)
print(all(nlis1))