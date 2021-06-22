import unittest

from pympcam.coralManager import CoralManager

class TestCoralManagerMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.coral = CoralManager()
        return super().setUp()

    def test_on(self):
        self.assertTrue(self.coral.turnOn())

    def test_off(self):
        self.coral.turnOff()
