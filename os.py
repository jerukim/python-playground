# unsafe approach
f = open('myfile.txt')
print(f.read())
f.close()


# safe approach
# opened file will only be available in code block
with open('myfile.txt') as f:
    text = f.read()

print(text)


# open file in "write" mode
def printFile(fileName: str):
    with open(fileName, 'r') as f:
        print(f.read())


with open('myfile.txt', 'w') as f:
    for i in range(1, 5):
        f.write(str(i))

printFile('myfile.txt')


# write new line
with open('myfile.txt', 'w') as f:
    for i in range(1, 5):
        f.write(f'Number {i}\n')

printFile('myfile.txt')


# append to file
with open('myfile.txt', 'a') as f:
    for i in range(5, 8):
        f.write(f'Append number {i}\n')

printFile('myfile.txt')


# read file to list
with open('myfile.txt') as f:
    lines = list(f)
    print(lines)
# or
with open('myfile.txt') as f:
    lines = f.readlines()
    print(lines)
