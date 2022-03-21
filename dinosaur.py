class Dinosaur:
    def __init__(self,name,attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack_robot(self,robot):
        robot.health -= 10
        print(f"{self.name} has attacked {robot.name}")
        print(f"{robot.name} current health is {robot.health} ")
