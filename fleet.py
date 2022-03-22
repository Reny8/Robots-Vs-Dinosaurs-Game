from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = [Robot("Titanium"), Robot("Steel"), Robot("Chromium")]
    
    def create_fleet(self):
        if len(self.robots) == 3:
            print(f"Type 0 for: {self.robots[0].name}, Health: {self.robots[0].health}")
            print(f"Type 1 for: {self.robots[1].name}, Health: {self.robots[1].health}")
            print(f"Type 2 for: {self.robots[2].name}, Health: {self.robots[2].health}")
        elif len(self.robots) == 2:
            print(f"Type 0 for: {self.robots[0].name}, Health: {self.robots[0].health}")
            print(f"Type 1 for: {self.robots[1].name}, Health: {self.robots[1].health}")
        elif len(self.robots) == 1:
            print(f"Type 0 for: {self.robots[0].name}, Health: {self.robots[0].health}")