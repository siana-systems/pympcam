import unittest

from pympcam.irLed import IrLed

class TestIrLedMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.ir = IrLed()
        return super().setUp()

    def test_on(self):
        self.ir.turnOn()
        self.assertTrue(self._readState())

    def test_off(self):
        self.ir.turnOff()
        self.assertFalse(self._readState())

    def _readState(self):
        return self.ir.irx.read()