from pympcam.commons import MpcamGpio
import logging

class IrLed:
    irx = MpcamGpio(5, 2, "out").init() # PF2
    
    def __init__(self):
        self.log = logging.getLogger(__name__)

    def turnOn(self) -> None:
        """
        Turns on IR LEDs
        """
        self.irx.write(True)
        self.log.debug(f"Turn IR on")

    def turnOff(self) -> None:
        """
        Turns off IR LEDs
        """
        self.irx.write(False)
        self.log.debug(f"Turn IR on")
