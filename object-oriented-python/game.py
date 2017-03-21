from char import Char
import debug
from monster import Dragon, Goblin, Troll, Orge
import sys

class Game:
    def setup(self):
        debug.log('Setting up!')
        self.player = Char()
        self.monsters = [
            Goblin(),
            Troll(),
            Orge(),
            Dragon()
        ]  
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        debug.log('Getting next monster!')
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        debug.log('Monsters Turn!')
        # Check to see if the monster attacks
        #if so tell the player
            # check if the player wants to dodge
            # if so see if dodge is successful
                # if it is move on
            # if its not, remove player hp
        # if the monster isnt attacking tell the player that to.
        if self.monster.attack():
            print("{} is attacking".format(self.monster))
            print(self.monster.battlecry())
            dodge = input("Do you want to dodge? [Y]es or [N]o").lower()
            if dodge == 'y':
                if self.player.dodge():
                    print("You dodged the attack!")
                else:
                    print("You have been hit!")
                    self.player.hp -= 1
            else:
                print("{} hit you for 1 hp".format(self.monster))
                self.player.hp -= 1
        else:
            print("{} isnt paying attention".format(self.monster))

    def player_turn(self):
        debug.log('Players Turn!')
        #let the player attack , rest or quit
        # if they attack
            # see if the attack is successful
                #if so see if monster dodges
                    # if dodged print that
                    #if not subtract right num from monster
                # if the attack is good tell the player
        # if they rest
            # call rest function
        # if they quit 
            # if they quit , quit the Game
        #rerun if anytthing else
        print("Your Turn!")
        choice = input("What would you like to do. [A]ttack, [R]est, [Q]uit").lower()
        if choice == 'a':
            print("You are attacking {}".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print("Monster dodged your attack!")
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= (self.player.dmg + 1)
                        print("You hit {} for {}".format(self.monster, (self.player.dmg + 1)))
                    else:
                        self.monster.hit_points -= self.player.dmg
                        print("You hit {} for {}".format(self.monster, self.player.dmg))
            else:
                print("You missed!")
        elif choice == 'r':
            self.player.rest()
        elif choice == 'q':
            sys.exit()
        else:
            self.player_turn()
    def cleanup(self):
        debug.log('Cleaning up!')
        # if the monster has no more hp:
            # up the players exp
            # print message
            # get new monster
        if self.monster.hit_points <= 0:
            self.player.exp += self.monster.experience
            print("You gained experience from {}!".format(self.monster))
            self.monster = self.get_next_monster()
        
    def __init__(self):
        debug.log('Game Init!')
        self.setup()

        while self.player.hp and (self.monster or self.monsters):
            print('\n'+'='*20)
            print(self.player)
            self.monster_turn()
            print('\n'+'-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)
        if self.player.hp:
            print("You win!")
        elif self.monsters or self.monster:
            print("You lose!")
        sys.exit()
Game()