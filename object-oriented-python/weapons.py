import random
import debug

class Weapon:
    min_dmg = 1
    max_dmg = 1
    weight = 1 

class Axe(Weapon):
    debug.log('Axe init called')
    name = 'Axe'
    min_dmg = 3
    max_dmg = 10
    weight = 7

class Sword(Weapon):
    debug.log('Sword init called')
    name = 'Sword'
    min_dmg = 2
    max_dmg = 6
    weight = 4

class Mace(Weapon):
    debug.log('Mace init called')
    name = 'Mace'
    min_dmg = 3
    max_dmg = 5
    weight = 3

class Crossbow(Weapon):
    debug.log('Crossbow init called')
    name = 'Crossbow'
    min_dmg = 4
    max_dmg = 7
    weight = 3

class Bow(Weapon):
    debug.log('Bow init called')
    name = 'Bow'
    min_dmg = 1
    max_dmg = 5
    weight = 2

class Katana(Weapon):
    debug.log('Katana init called')
    name = 'Katana'
    min_dmg = 2
    max_dmg = 6
    weight = 2

class Knife(Weapon):
    debug.log('Knife init called')
    name = 'Knife'
    min_dmg = 1
    max_dmg = 3
    weight = 1