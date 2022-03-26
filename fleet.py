from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = [Robot("Titanium"), Robot("Steel"), Robot("Chromium")]
    
    def create_fleet(self):
        counter = 0
        for robot in self.robots:
            print(f"Type {counter} for: {robot.name}, Health: {robot.health}")
            counter += 1