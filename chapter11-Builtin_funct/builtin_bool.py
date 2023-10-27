lis, dict, tuple = [], {}, ()
print(bool(lis), bool(dict), bool(tuple))

lis, dict, tuple = [0], {'a':1}, (1,)
print(bool(lis), bool(dict), bool(tuple))

lis, dict, tuple = [0.0], {'a':1.0}, (1.0,)
print(bool(lis), bool(dict), bool(tuple))

a,b,c = 0, 3.14, 'Hello, Python!'
print(bool(a), bool(b), bool(c))
#statement = None
print(bool(None))
true = True
print(bool(true))