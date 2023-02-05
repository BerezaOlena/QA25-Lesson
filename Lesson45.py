import random

class Gender:
    male = 'male'
    female = 'female'

class User:
    name = ['Sten', 'Ben', 'Den', 'Glen']
    surname = ['Smith', 'Butler', 'Fisher', 'Batcher']

    def __init__(self, nick='', email='', password='', gender=''):

        if not gender:
            self.gender = Gender.male
        else:
            self.gender = gender

        if not nick:
            self.nick = random.choice(self.name) + '_' + random.choice(self.surname)
        else:
            self.nick = nick

        if not email:
            self.email = (self.nick).lower() + '@gmail.com'
        else:
            self.email = email

        if not password:
            self.password = (random.choice(self.name))[random.randint(0, 2)] + \
                        ((random.choice(self.name))[random.randint(0, 2)]).upper() + \
                        ((random.choice(self.name))[random.randint(0, 2)]).lower() + \
                        str(random.randint(0, 9)) + \
                        str(random.randint(0, 9)) + \
                        str(random.randint(0, 9))
        else:
            self.password = password