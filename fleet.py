from robot import Robot
class Fleet:
    def __init__(self):
        self.robots = []
    
    def create_fleet(self):
        robot_1 = Robot("Titanium")
        robot_2 = Robot("Steel")
        robot_3 = Robot("Chromium")
        self.robots.append(robot_1)
        self.robots.append(robot_2)
        self.robots.append(robot_3)
        

