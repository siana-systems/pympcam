import unittest

from pympcam.headerPwm import HeaderPwm

class TestHeaderPwmMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.pwm = HeaderPwm()
        return super().setUp()

    def test_enable_pwm1(self):
        self.pwm.enable("pwm1")
    
    def test_get_pwm1(self):
        expected = (1, 1)
        self.pwm.enable("pwm1", frequency=expected[1], duty_cycle=expected[0])
        ret = self.pwm.get("pwm1")
        self.assertEqual(expected, ret)
    
    def test_enable_pwm2(self):
        self.pwm.enable("pwm2")

    def test_get_pwm2(self):
        expected = (1, 2)
        self.pwm.enable("pwm2", frequency=expected[1], duty_cycle=expected[0])
        ret = self.pwm.get("pwm2")
        self.assertEqual(expected, ret)