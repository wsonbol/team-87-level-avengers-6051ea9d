from unittest import TestCase
from levelup.position import Position


class TestPosition(TestCase):
    def test_init(self):
        testObj = Position()
        assert testObj.current_position != None


