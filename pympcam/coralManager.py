
from pympcam.commons import MpcamGpio

from time import sleep
import logging

class CoralManager:
    TIMEOUT_PGOOD_SEC = 0.002
    TIMEOUT_RST_SEC = 0.01
    TIMEOUT_PWR_EN_SEC = 0.01
    
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.PWR_EN = MpcamGpio(9, 1, "out").init() # PZ1
        self.PMIC_EN = MpcamGpio(7, 15, "out").init()  # PH15
        self.RST_L = MpcamGpio(4, 14, "out").init() # PE14
        self.PGOOD4 = MpcamGpio(8, 2, "in").init() # PI2
    
    def turnOn(self) -> bool:
        """
        Turns on internal Coral device in MPCam.
        Power up sequence based on :
        https://coral.ai/static/files/Coral-Accelerator-Module-datasheet.pdf

        :returns: PGOOD4 state, should be True to indicate proper turn on.
        """
        self.log.info("Powering coral up")
        # 0. Set defaul state for pins
        self._initPins()
        # 1. SET pin CORAL_PWR_EN (PZ1)
        self.log.debug("Enabling PWR_EN")
        self.PWR_EN.write(True)
        # 2. Wait 10mS
        sleep(self.TIMEOUT_PWR_EN_SEC)
        # 3. SET pin CORAL_PMIC_EN (PH15)
        self.log.debug("Enabling PMIC_EN")
        self.PMIC_EN.write(True)
        # 4. RSTL_L after 10 ms
        sleep(self.TIMEOUT_RST_SEC)
        self.RST_L.write(True)
        # Check PGOOD4 (not needed at this point, just for good measure)
        ret = self.PGOOD4.read()
        self.log.debug(f"PGOOD4 is {ret}")
        return ret
    
    def turnOff(self):
        """
        Turns off internal Coral device in MPCam.
        """
        self.log.info("Powering coral down")
        pins = [self.RST_L, self.PMIC_EN, self.PWR_EN]
        for pin in pins:
            self.log.debug(f"Disabled {pin}")
            pin.write(False)

    def _initPins(self):
        self.log.debug("Setting initial state for pins")
        pins = [self.PWR_EN, self.PMIC_EN, self.RST_L]
        for pin in pins:
            self.log.debug(f"Disabled {pin}")
            pin.write(False)
