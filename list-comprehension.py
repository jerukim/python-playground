evens = [x for x in range(1, 10) if x % 2 == 0]

print(evens)

numsPlusFour = [x + 4 for x in [10, 20]]

print(numsPlusFour)


def some_function(a):
    return (a + 5) / 2


m = [some_function(x) for x in range(8)]

print(m)
