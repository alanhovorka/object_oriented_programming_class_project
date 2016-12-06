from armory import Armory
from kitchen import Kitchen
from entry import EntryWay
from dining_room import DiningRoom
from courtyard import Courtyard
from walls import Walls
from bedroom import Bedroom
from rec import Rec
import random

class Character:
    """docstring for Character"""
    def __init__(self, name, health, attack_pts):
        self.name = name
        self.health = health
        self.attack_pts = attack_pts

    def combat(self, defender):
        dead = ''
        attack = int(random.random()*self.attack_pts)
        defense = int(random.random()*defender.attack_pts)
        if attack > defense:
            defender.health -= attack
            print("\n{} suffered {} damage. {}'s health is now at {} \n".format(defender.name, attack, defender.name, defender.health))
        elif attack < defense:
            self.health -= defense
            print("\n{}sufferecd {} damage. {}'s health is now at {}\n".format(self.name, defense, self.name, self.health))
        else:
            print("No damage")
        if self.health < 1:
            dead = self.name
        elif defender.health < 1:
            dead = defender.name
        if dead:
            print("\n{} has been killed!\n".format(dead))
            return dead

    