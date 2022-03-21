from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []
    
    def create_herd(self):
        dino_1 = Dinosaur("T-Rex", 60)
        dino_2 = Dinosaur("Raptor", 30)
        dino_3 = Dinosaur("Pteridactyl", 10)
        self.dinosaurs.append(dino_1)
        self.dinosaurs.append(dino_2)
        self.dinosaurs.append(dino_3)


