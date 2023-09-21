class Character:
    name = ""

    def __init__(self, character_name):
        self.name = character_name
        self.position = None

    def getName(self):
        self.name

    def Character(character: str):
        self.name=character

    def move(self, direction):
        if not self.game_map:
            print(f"{self.name} is not on any map!")
            return

        # Define movement directions
        movements = {
            'up': (0, 1),
            'down': (0, -1),
            'left': (-1, 0),
            'right': (1, 0),
        }
        
        dx, dy = movements.get(direction, (0, 0))
        new_position = (self.position[0] + dx, self.position[1] + dy)
        
        if self.game_map.isPositionValid(new_position):
            self.position = new_position
            print(f"{self.name} has moved {direction} to position {new_position}!")
        else:
            print(f"{self.name} can't move {direction}!")

    def enterMap(self, game_map, position=(0, 0)):
        if game_map.isPositionValid(position):
            self.position = position
            print(f"{self.name} has entered the map at position {position}!")
        else:
            raise ValueError(f"The position {position} is not valid in the map!")

    def getPosition(self):
        if self.position:
            return self.position
        return f"{self.name} hasn't entered the map yet."