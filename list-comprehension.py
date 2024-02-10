# basic examples
evens = [x for x in range(1, 10) if x % 2 == 0]

print(evens)

numsPlusFour = [x + 4 for x in [10, 20]]

print(numsPlusFour)


def some_function(a):
    return (a + 5) / 2


m = [some_function(x) for x in range(8)]

print(m)


# advanced examples

# nested list comprehension
m = [[j for j in range(3)] for i in range(4)]
print(m)

# flatten nested list
n = [value
     for sublist in m
     for value in sublist]
print(n)


# set comprehensions
s = {s for s in range(1, 5) if s % 2}
print(s)
