import os

# create file
open('myfile.txt', 'x').close()

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


# read file as iterator
with open('myfile.txt', 'r') as f:
    for line in f:
        print(line)


# check if file exists
if os.path.isfile('myfile.txt'):
    print('the file exists')

if os.path.isfile('nothere.txt'):
    print('the file exists')

# create a directory
try:
    os.mkdir('mydir')
except FileExistsError as e:
    print(e)

# check if directory exists
if os.path.isdir('mydir'):
    print('the directory exists')

# delete file
# os.remove('myfile.txt')


# rename file
os.rename('myfile.txt', 'renamed.txt')


# move file
os.rename('renamed.txt', './mydir/myfile.txt')
