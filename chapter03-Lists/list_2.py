nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
print('Before changing:', nlis)
nlis[0] = 'hello python!'       #replace #0
print('After changing:', nlis)
nlis[1] = 1.618                 #replace #1
print('After changing:', nlis)
nlis[2] = [3.14, 2022]          #replace #2
print('After changing:', nlis)

print()
#Delete
print("Delete opetrations:")

print('Before chnaging:',  nlis)
del(nlis[0])
print('After chnaging:',  nlis)
del(nlis[-1])
print('After chnaging:',  nlis)
del nlis
print("list deleted")