# from time import sleep
import json
import traceback

try:
    print(2 / 0)
except ZeroDivisionError:
    print('You caant divide by zero idiot')

try:
    f = open('myfile.txt', 'r')
    f.write('hello world')
except IOError as e:
    print('an error occured:', e)
finally:
    print('closing the file like a good boy')
    f.close()

# while True:
#     try:
#         print('try and stop me')
#         sleep(1)
#     except Exception:
#         print('cant stop wont stop')

user_json = '{"name": "jeru", "age": 28}'
user = json.loads(user_json)

try:
    print(user['name'])
    print(user['age'])
    print(user['address'])
except KeyError as e:
    print('there are missing fields', e)


class UserNotFoundError(Exception):
    pass


def fetch_user(user_id):
    user = None

    if user == None:
        raise UserNotFoundError(f'user {user_id} not in db')
    else:
        return user


users = [123, 456, 789]

for user_id in users:
    try:
        fetch_user(user_id)
    except UserNotFoundError as e:
        # print('there was an error: ', e)
        traceback.print_exc()

# why is using a regular Exception object here a bad idea?
# 1. The error would not be as clear
# 2. You wouldn't able to tell the difference between another exception case
