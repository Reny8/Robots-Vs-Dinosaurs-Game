from weapon import Weapon
class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Lasers",20)

    def attack_dinosaur(self,dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{self.name} has attacked {dinosaur.name}")
        print(f"{dinosaur.name} current health is {dinosaur.health}")

    def choose_weapon(self):
        list = [Weapon("Grenades",40), Weapon("Lethal Darts", 60), Weapon("Lasers", 20)]
        print(f"Type 0 for {list[0].name}, Attack Strength: {list[0].attack_power}. ")
        print(f"Type 1 for {list[1].name}, Attack Strength: {list[1].attack_power}. ")
        print(f"Type 2 to continue with the default weapon: {list[2].name}, Attack Strength: {list[2].attack_power}.")

        weapon_choice = int(input("Choose a weapon for your Robot: "))
        if weapon_choice == 0:
            self.weapon = Weapon("Grenades", 40)
            print("Your new weapon is Grenades! ")
        elif weapon_choice == 1:
            self.weapon = Weapon("Lethal Darts",60)
            print("Cool! Your new weapon is Lethal Darts! ")
        elif weapon_choice == 2:
            self.weapon = Weapon("Lasers", 20)
            print("Your weapon will remain the same. ")