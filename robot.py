from weapon import Weapon
from dinosaur import Dinosaur
class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Sword", 100)

    def attack_dinosaur(self,dinosaur):
        dinosaur.health -= 10
        print(f"{self.name} has attacked {dinosaur.name}")
        print(f"{dinosaur.name} current health is {dinosaur.health}")

robot_1 = Robot("Bot")
dino_1 = Dinosaur("Rex", 100)
robot_1.attack_dinosaur(dino_1)
robot_1.attack_dinosaur(dino_1)