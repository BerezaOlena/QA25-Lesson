import random
class User:
    names = ['John3', 'Sten3', 'Tim3', 'Bill3']
    surnames = ['Doe', 'Mustermann', 'Freeman', 'Smith']
    def __init__(self):
        self.nick = random.choice(self.names) + random.choice(self.surnames)
        self.email = (self.nick).lower() + '@gmail.com'
        self.password = (random.choice(self.names))[random.randint(0, 2)] + \
                        (random.choice(self.names))[random.randint(0, 2)] + \
                        (random.choice(self.names))[random.randint(0, 2)] + \
                        ((random.choice(self.names))[random.randint(0, 2)]).upper() + \
                        ((random.choice(self.names))[random.randint(0, 2)]).lower() + \
                        str(random.randint(0, 9)) + \
                        str(random.randint(0, 9)) + \
                        str(random.randint(0, 9))
if __name__ == '__main__':
    a = User()
    print(a.nick, a.email, a.password)


