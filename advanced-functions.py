# forced keyword arguments
def fKeyword(*, a, b):
    print(a, b)


try:
    fKeyword(1, 2)
except TypeError as e:
    print('error:', e)

# unpack dictionary key/values as keyword arguments
args = {'a': 1, 'b': 2}
fKeyword(**args)


# unpack list values as positional arguments
def fPositional(a, b, c):
    print(a, b, c)


l = [1, 2, 3]
fPositional(*l)


# decorating functions
def print_argument(func):
    def wrapper(the_number):
        print('argument for', func.__name__, 'is', the_number)
        return func(the_number)

    return wrapper


@print_argument
def add_one(x):
    return x + 1


print(add_one(1))


# anonymous functions, aka: lambda
add_one = (lambda x: x + 1)
add_one(3)

numbers = [1, 2, 3, 4]
times_two = map(lambda x: x * 2, numbers)
print(times_two)
print(list(times_two))
