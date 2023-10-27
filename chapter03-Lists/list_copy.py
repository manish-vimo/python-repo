# The element in the copied list also changes when the element in the original list was changed.

nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]

copy_list = nlis

print('nlis:', nlis)
print('copy_nlis:', copy_list)


print('copy_list[0]:', copy_list[0])
nlis[0] = 'hello python!'
print('nlis[0]:', nlis[0])
print('copy_list[0]:', copy_list[0]) 

