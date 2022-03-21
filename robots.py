from weapon import Weapon
from dinosaur import Dinosaur
class Robots:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Sword", 100)

    def attack(self,dinosaur):
        dinosaur.health -= 10
        print(f"{self.name} has attacked {dinosaur.name}")
        print(f"{dinosaur.name} current health is {dinosaur.health}")

robot_1 = Robots("Roger")
dino_1 = Dinosaur("Rex",100)
robot_1.attack(dino_1)
