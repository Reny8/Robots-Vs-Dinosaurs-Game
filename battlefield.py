from fleet import Fleet
from herd import Herd
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        # NOT DONE WITH YET
    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs! ")
        
    def battle(self):
        pass

    def dino_turn(self,dinosaur):
        pass

    def robo_turn(self,robot):
        pass

    def show_dino_opponent_options(self):
        self.fleet.create_fleet()
        print("Robot Opponents")
        for robo in self.fleet.robots:
            print(f"Name: {robo.name}, Health: {robo.health}")
    def show_robo_opponent_options(self):
        print("Dino Opponents")
        self.herd.create_herd()
        for dino in self.herd.dinosaurs:
            print(f"Name: {dino.name}, Health: {dino.health}")
    def display_winners(self):
        pass
