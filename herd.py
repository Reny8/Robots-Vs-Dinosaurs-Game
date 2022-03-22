from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = [Dinosaur("T-Rex", 60),Dinosaur("Raptor", 30), Dinosaur("Pteridactyl", 10)]
    
    def create_herd(self):
        if len(self.dinosaurs) == 3:
            print(f"Type 0 for: {self.dinosaurs[0].name}, Health: {self.dinosaurs[0].health}")
            print(f"Type 1 for: {self.dinosaurs[1].name}, Health: {self.dinosaurs[1].health}")
            print(f"Type 2 for: {self.dinosaurs[2].name}, Health: {self.dinosaurs[2].health}")
        elif len(self.dinosaurs) == 2:
            print(f"Type 0 for: {self.dinosaurs[0].name}, Health: {self.dinosaurs[0].health}")
            print(f"Type 1 for: {self.dinosaurs[1].name}, Health: {self.dinosaurs[1].health}")
        elif len(self.dinosaurs) == 1:
            print(f"Type 0 for: {self.dinosaurs[0].name}, Health: {self.dinosaurs[0].health}")

        
