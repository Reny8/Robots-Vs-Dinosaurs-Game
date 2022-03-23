from fleet import Fleet
from herd import Herd
import random
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
    
    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs! ")

    def battle(self):
        turns = [self.dino_turn, self.robo_turn]
        game_not_over = True
        while game_not_over == True:
            random.choice(turns)()
            if len(self.fleet.robots) == 0:
                self.display_winners("Dinosaurs")
                game_not_over = False
            elif len(self.herd.dinosaurs) == 0:
                self.display_winners("Robots")
                game_not_over = False

    def dino_turn(self):
        self.show_robo_opponent_options()
        dino_index = int(input("Choose your Dinosaur: "))
        self.show_dino_opponent_options()
        robot_index = int(input("Choose the Robot you want to attack: "))
        self.herd.dinosaurs[dino_index].attack_robot(self.fleet.robots[robot_index])
        if self.fleet.robots[robot_index].health <= 0:
            print(f"Your have killed {self.fleet.robots[robot_index].name}!")
            self.fleet.robots.remove(self.fleet.robots[robot_index])
            

    def robo_turn(self):
        self.show_dino_opponent_options()
        robot_index = int(input("Choose your Robot: "))
        self.fleet.robots[robot_index].choose_weapon()
        self.show_robo_opponent_options()
        dino_index = int(input("Choose the Dinosaur you want to attack: "))
        self.fleet.robots[robot_index].attack_dinosaur(self.herd.dinosaurs[dino_index])
        if self.herd.dinosaurs[dino_index].health <= 0:
            print(f"You have killed {self.herd.dinosaurs[dino_index].name}! ")
            self.herd.dinosaurs.remove(self.herd.dinosaurs[dino_index])


    def show_dino_opponent_options(self):
        self.fleet.create_fleet()

    def show_robo_opponent_options(self):
        self.herd.create_herd()

    def display_winners(self, winning_team):
        print(f"{winning_team} have won the fight! Game over. ")
