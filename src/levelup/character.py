class Character:
    name = ""

    def __init__(self, character_name):
        self.name = character_name
        self.position = None

    def getName(self):
        self.name

    def Character(character: str):
        self.name=character

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        pass

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