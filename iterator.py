# under the hood
try:
    iterable = range(1, 3)
    iterator = iterable.__iter__()
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
except StopIteration as e:
    print('naur more items', e)
