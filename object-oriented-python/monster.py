# class Monster(object): optional
import random
import debug

COLORS = ['yellow','red','blue','green','orange','black','white']

#two spaces between class and constant is pep 8 compliance
# add (object) to work in python 2 and 3 at the smae time
from combat import Combat

class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):        
        debug.log('Monster init called')
        #kwargs trys to get a default out and if it cant the second arguemnet is set
        #self.hit_points = kwargs.get('hit_points', 1)
        #self.color = kwargs.get('color', 'yellow')
        #self.weapon = kwargs.get('weapon', 'sword')
        #self.sound = kwargs.get('sound', 'rawr')
        self.hit_points = random.randint(self.min_hit_points, self.max_hit_points)
        self.experience = random.randint(self.min_experience, self.max_experience)
        self.color = random.choice(COLORS)

        # if anything else comes in and is not set set it 
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{} {}, HP: {}, XP: {}'.format(self.color.title(),self.__class__.__name__,self.hit_points, self.experience)

    def battlecry(self):
        debug.log('Monster battlecry called')
        return self.sound.upper()

class Goblin(Monster):
    debug.log('Monster goblin init called')
    max_hit_points = 3
    max_experience = 2
    sound = 'squak!' 
    # pass #add pass if you pass nothing in

class Troll(Monster):
    debug.log('Monster Troll init called')
    min_hit_points = 3
    max_hit_points = 5
    min_experience = 2
    max_experience = 6
    sound = 'growl!'

class Orge(Monster):
    debug.log('Monster orge init called')
    min_hit_points = 3
    max_hit_points = 7
    min_experience = 4
    max_experience = 8
    sound = 'me numbskull!'

class Dragon(Monster):
    debug.log('Monster Dragon init called')
    min_hit_points = 5
    max_hit_points = 10
    min_experience = 6
    max_experience = 10
    sound = 'rararararrrrrrrrr!'
