from math import sqrt
class Time: #imo usless mozna zwykly time policzyc

    sol = 36 #trzeba sprawdzic czy rell

    def __init__(self, day, hours, minuts):
        self.day = day
        self.hour = hours
        self.minuts = minuts
    
    def __init__(self, hours, minuts):
        self.day = 0
        self.hour = hours
        self.minuts = minuts

    def __init__(self, minuts):
        self.day = 0
        self.hour = 0
        self.minuts = minuts

    def hours_to_mars_days(self, hours):
        if hours >= Time.sol:
            self.day += 1
            self.hour -= Time.sol
    

class Position:
    def __init__(self, x_position, y_position):
        self.x = x_position
        self.y = y_position

class Poi:
    def __init__(self, time_of_task: Time, position: Position, priority_level: int):
        self.time_of_task = time_of_task
        self.position = position
        self.priority_level = priority_level
    
    @classmethod
    def check_distance_to_node(self, rover_position):
        return sqrt((self.position.x - rover_position.x) ** 2 + (self.position.y - rover_position.y) ** 2)