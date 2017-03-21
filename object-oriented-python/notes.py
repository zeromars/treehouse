# everything in python is a object

from monster import Monster
Monster.hit_points
# 1
Monster.color
# 'yellow'
Monster.weapon
# 'sword'
jubjub = Monster()
type(jubjub)
# <class 'monster.Monster'>
jubjub.hit_points
# 1
jubjub.hit_points = 5
jubjub.hit_points
# 5
jabberwock = Monster()
jabberwock.hit_points
# 1

# error because you arent calling it on a instance of a class
Monster.battlecry()
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: battlecry() missing 1 required positional argument: 'self'

jubjub = Monster()
jubjub.battlecry()
# 'ROAR'
jubjub.sound = "tweet"
jubjub.battlecry()
# 'TWEET'

class Store:
    open = 9
    close = 5
    
    def hours(self):
        return "We're open from {} to {}".format(self.open, self.close)

# dunderinit == __init__ (double underscore)

# def __init__(self, hit_points, weapon, color, sound):
jabberwock = Monster(6, 'mace', 'red', 'rawr')
jabberwock.battlecry()
# 'RAWR'

# def __init__(self, hit_points=5, weapon='sword', color='yellow', sound='rawr'):
jabberwock = Monster(10)
jabberwock.battlecry()
# 'RAWR'
jabberwock.hit_points
# 10

# def __init__(self, **kwargs):
troll = Monster(color='green',sound="grrrr")
troll.battlecry()
# 'GRRRR'

jubjub = Monster()
jubjub.hit_points
# 1
jubjub.color
#'orange'

orge = Monster(color='orange', hit_points= 500, adjective='ugly')
orge.hit_points
# 500
orge.adjective
# 'ugly'

azog = monster.Goblin()
snaga = monster.Troll()
pete = monster.Dragon()
pete.hit_points
# 5
snaga.experience
# 4

# Group common operations into functions
# Group common functionality into classes