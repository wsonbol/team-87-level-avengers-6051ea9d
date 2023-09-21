import logging
from dataclasses import dataclass

class Position:
    current_position: tuple 

    def __init__(self):
        self.current_position = (-100,-200)
 
