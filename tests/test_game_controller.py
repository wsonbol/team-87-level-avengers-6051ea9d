from unittest import TestCase
from levelup.controller import GameController

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None
    
    def test_move(self):
        startPostion = (0, 0)
        endingPosition = (1, 0)
        
        testObj = GameController.move(startPostion, endingPosition)
        self.assertNotEquals(startPostion, endingPosition)
