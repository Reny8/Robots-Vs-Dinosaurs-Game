from weapon import Weapon
class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Sword", 100)

    def attack_dinosaur(self,dinosaur):
        dinosaur.health -= 10
        print(f"{self.name} has attacked {dinosaur.name}")
        print(f"{dinosaur.name} current health is {dinosaur.health}")
