# The cloned list is a new copy or clone of the original list.
nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
clone_list = nlis[:]
print(clone_list)


# When an element in the original list is changed, the element in the cloned list does not change.
print(nlis)
print('clone_list[0]:', clone_list[0])
nlis[0] = 'hello, python!'
print('nlis[0]:', nlis[0])
print('clone_list[0]:', clone_list[0])