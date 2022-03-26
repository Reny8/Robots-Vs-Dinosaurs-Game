from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = [Dinosaur("T-Rex", 60),Dinosaur("Raptor", 30), Dinosaur("Pteridactyl", 10)]
    
    def create_herd(self):
        counter = 0
        for dinosaur in self.dinosaurs:
            print(f"Type {counter} for: {dinosaur.name}, Health: {dinosaur.health}")
            counter += 1

        
