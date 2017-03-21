import random
import debug
from combat import Combat
from weapons import Axe, Sword, Mace, Crossbow, Bow, Katana, Knife 

class Char(Combat):
    attack_limit = 10
    exp = 0
    base_hp = 10
    weapons = [
        Axe(),
        Sword(),
        Mace(),
        Crossbow(),
        Bow(),
        Katana(),
        Knife()
    ]

    def get_dmg(self):
        debug.log('Get Damage called')
        dmg = random.randint(self.weapon.min_dmg, self.weapon.max_dmg)
        return dmg

    def get_weapon(self):
        debug.log('Get Weapon called')
        weapon = random.choice(self.weapons)
        return weapon

    def attack(self):
        debug.log('Char attack called')
        attack = self.get_dmg()
        return attack > 3

    #def get_weapon(self):
    #    debug.log('Char get weapon called')
    #    weapon_choice = input("Weapon ([S]word, [A]xe, [B]ow): ").lower()
    #    
    #    if weapon_choice in 'sab':
    #        if weapon_choice == 's':
    #            return 'sword'
    #        elif weapon_choice == 'a':
    #            return 'axe'
    #        else:
    #            return 'bow'
    #    else:
    #        return self.get_weapon()

    def __init__(self, **kwargs):
        debug.log('Char init called')
        self.name = input("Name: ")
        #self.weapon = self.get_weapon()
        self.weapon = self.get_weapon()
        self.dmg = self.get_dmg()
        self.weight = self.weapon.weight
        self.hp = self.base_hp
        print('Your weapon is a [{}] with dmg of {}, and a weight of {}'.format(self.weapon.name, self.dmg, self.weight))

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(self.name, self.hp, self.exp)

    def rest(self):
        debug.log('Char rest called')
        if self.hp < self.base_hp:
            self.hp += 1
    
    def leveled_up(self):
        debug.log('Char leveled called')
        return self.exp >= 5