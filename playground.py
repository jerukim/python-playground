import sys
from module import my_function, greeter
import package.subpackage1
from httptools.client import get
from httptools import client

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    name = 'stranger'

print(f'Hi there, {name}')


def test():
    a = 'a'

    def me():
        nonlocal a
        a += 'b'

    me()

    print(a)


test()

my_function()

get()
client.get()
