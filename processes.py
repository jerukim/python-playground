import subprocess

# list current directories and files with terminal command
subprocess.run(['ls', '-al'])


# run python
result = subprocess.run(['python', '--version'],
                        capture_output=True, encoding='UTF-8')

print(result)


# run code in subprocess
code = """
for i in range(1, 3):
    print(f'hello world {i}')
"""

result = subprocess.run(['python'], input=code,
                        capture_output=True, encoding='UTF-8')

print(result.stdout)
print(result.stdout)

# run shell command
result = subprocess.run(['ls -al | head -n 1'], shell=True)
print(result)


# vulnerable to command injection
thedir = input()
result = subprocess.run([f'ls -al {thedir}'], shell=True)
print(result)
