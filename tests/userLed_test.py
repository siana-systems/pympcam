import unittest

from pympcam.userLed import UserLed

class TestUserLedMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.led = UserLed()
        return super().setUp()

    def test_on(self):
        self.led.turnOn()
        ret = self.led.getState("led1") and self.led.getState("led2")
        self.assertTrue(ret)

    def test_off(self):
        self.led.turnOff()
        ret = self.led.getState("led1") and self.led.getState("led2")
        self.assertFalse(ret)

    def test_onLed1(self):
        self.led.turnOn("led1")
        self.assertTrue(self.led.getState("led1"))

    def test_offLed1(self):
        self.led.turnOff("lEd1")
        self.assertFalse(self.led.getState("lEd1"))

    def test_onLed2(self):
        self.led.turnOn("led2")
        self.assertTrue(self.led.getState("led2"))

    def test_offLed2(self):
        self.led.turnOff("led2")
        self.assertFalse(self.led.getState("led2"))
    
    def test_onLed2a(self):
        self.led.turnOn("Led2")
        self.assertTrue(self.led.getState("led2"))

    def test_onLed2b(self):
        self.led.turnOn("LED2")
        self.assertTrue(self.led.getState("led2"))

    def test_onLed2b(self):
        self.led.turnOn("LeD2")
        self.assertTrue(self.led.getState("led2"))

    def test_on_x(self):
        self.led.turnOn()
        ret = self.led.getState("led1") and self.led.getState("led2")
        self.assertTrue(ret)

    def test_offLedx(self):
        with self.assertRaises(Exception):
            self.led.turnOff("ledx")

    def test_onLedx(self):
        with self.assertRaises(Exception):
            self.led.turnOn("ledx")

    def test_disableHeartbeat(self):
        self.led.disableHeartbeat()
        self.assertFalse(self.led.getState("led1"))
