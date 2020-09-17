'''
Практика по написанию декоратора на примере логирования сообщений пользователей.
'''

from datetime import datetime
import os


def logger(func):
    def wrapper(obj, msg):
        func(obj, msg)
        if not os.path.exists('log.txt'):
            _ = open('log.txt', 'w').close()
            
        with open('log.txt', 'a') as f:
            date_time = datetime.strftime(datetime.today(), '%d.%m.%y %H:%M:%S')
            timestamp = int(datetime.today().timestamp())
            log = f'[{date_time}] | {timestamp} | {obj.ID} | {obj.name} | {msg}\n'
            f.write(log)
    return wrapper


class User:
    '''
    Класс, представляющий юзера. 
    Состоит из имени, id и возможности отправлять сообщения в консоль.
    '''
    users = [] 

    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        self.__class__.users.append(self)

    
    def __repr__(self):
        return f'User({self.ID}, {self.name})'


    @logger
    def send_message(self, msg):
        print(msg)



if __name__ == '__main__':
    
    import random
    
    USERS_NAME_SET = [
    'Peter', 
    'Artem', 
    'Roman', 
    'Alex', 
    'Anna', 
    'Kate', 
    'Sam',
    'John',
]

    while True:
        msg = input()
        if msg == 'STOP!!!':
            os.remove('log.txt')
            print(User.users)
            break
        
        user = User(random.randint(0, 100), random.choice(USERS_NAME_SET))
        user.send_message(msg)