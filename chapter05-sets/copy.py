set8 = {1,3,5,7,9}
print(set8)
set9 = set8
print(set9)
set8.add(11)
print(set8)
print(set9)

"""
As you see that although the number 8 is added into the set 'set8', the added number
is also added into the set 'set9'
"""

print()

set10 = {1,3,5,7,9}
print(set10)
set9 = set10.copy()
print(set9)
set10.add(11)
print(set10)
print(set9)
"""
When this function is used, the original set stays unmodified.
A new copy stored in another set of memory locations is created.
The change made in one copy won't reflect in another.
"""