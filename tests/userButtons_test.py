import unittest

from pympcam.userButtons import UserButtons

class TestUserButtonsMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.btn = UserButtons()
        return super().setUp()

    def test_getSW(self):
        ret = self.btn.getState()
        self.assertFalse(ret[0] and ret[1])

    def test_getSW1(self):
        ret = self.btn.getState("sw1")
        self.assertFalse(ret)
    
    def test_getSW2(self):
        ret = self.btn.getState("sw2")
        self.assertFalse(ret)

    def test_getSWx(self):
        with self.assertRaises(Exception):
            self.btn.getState("swx")

    def test_pollSW2(self, timeout_sec=10):
        print(f"\nPress SW2 during the next {timeout_sec} seconds")
        ret = self.btn.pollState(self.btn.SW2)
        self.assertTrue(ret)
