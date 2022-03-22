from fleet import Fleet
from herd import Herd
import random
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

    def dino_turn(self):
        self.show_robo_opponent_options()
        dino_index = int(input("Choose your Dinosaur: "))
    
        self.show_dino_opponent_options()
        robot_index = int(input("Choose the Robot you want to attack: "))
        self.herd.dinosaurs[dino_index].attack_robot(self.fleet.robots[robot_index])


    def robo_turn(self):
        self.show_dino_opponent_options()
        robo_choice = input("Choose your Robot: ")

        self.show_robo_opponent_options()
        chosen_dino_to_attack = input("Choose the Dinosaur you want to attack: ")


    def show_dino_opponent_options(self):
        self.fleet.create_fleet()
        print(f"Type 0 for: {self.fleet.robots[0].name}, Health: {self.fleet.robots[0].health}")
        print(f"Type 1 for: {self.fleet.robots[1].name}, Health: {self.fleet.robots[1].health}")
        print(f"Type 2 for: {self.fleet.robots[2].name}, Health: {self.fleet.robots[2].health}")

    def show_robo_opponent_options(self):
        self.herd.create_herd()
        print(f"Type 0 for: {self.herd.dinosaurs[0].name}, Health: {self.herd.dinosaurs[0].health}")
        print(f"Type 1 for: {self.herd.dinosaurs[1].name}, Health: {self.herd.dinosaurs[1].health}")
        print(f"Type 2 for: {self.herd.dinosaurs[2].name}, Health: {self.herd.dinosaurs[2].health}")

    def display_winners(self):
        pass

battle = Battlefield()
battle.dino_turn()