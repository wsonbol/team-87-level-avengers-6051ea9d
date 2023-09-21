class GameMap:
    def __init__(self, grid):
        self.grid = grid  # 2D grid/map of the game
    
    def getPosition(self, item):
        for i, row in enumerate(self.grid):
            if item in row:
                return (i, row.index(item))
        return None  # Return None if the item is not found in the grid

    def calculatePosition(self, starting_position, direction):
        x, y = starting_position
        
        # Define direction movements
        movements = {
            'up': (0, 1),
            'down': (0, -1),
            'left': (-1, 0),
            'right': (1, 0),
        }
        
        # Calculate the new position
        dx, dy = movements.get(direction, (0, 0))
        new_position = (x + dx, y + dy)
        
        # Validate the new position (you can also check other conditions like obstacles if needed)
        if 0 <= new_position[0] < len(self.grid) and 0 <= new_position[1] < len(self.grid[0]):
            return new_position
        else:
            raise ValueError("New position is out of the grid bounds.")

    def isPositionValid(self, position):
        x, y = position
        if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):
            return True
        return False

    def getTotalPositions(self):
        return len(self.grid) * len(self.grid[0]) if self.grid else 0