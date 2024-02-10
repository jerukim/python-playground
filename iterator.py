# under the hood
try:
    iterable = range(1, 3)
    iterator = iterable.__iter__()
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
except StopIteration as e:
    print('naur more items', e)


mystring = 'abc'
for letter in mystring:
    print(letter)

mylist = ['a', 'b', 'c']
for letter in mystring:
    print(letter)

print([x for x in 'abc'])
print([x for x in [1, 2, 3, 4] if x > 2])

d = {'name': 'Alice', 'age': 23, 'country': 'NL'}
for key in d:
    print(key)

for val in d.values():
    print(val)

for key, val in d.items():
    print(key, val)

print([f'{k}: {v}' for k, v in d.items()])

# converting iterators
l = list(range(1, 4))
print(l)
s = set(range(1, 4))
print(s)
t = tuple(range(1, 4))
print(t)
