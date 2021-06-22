from periphery import GPIO
from dataclasses import dataclass

@dataclass
class MpcamGpio:
    """
    Data class for MPCam GPIO.

    :todo: Verify which periphery version has inverted gpio https://python-periphery.readthedocs.io/en/latest/gpio.html

    :param chip: Chip number for the GPIO.
    :param pin: Pin number for the GPIO chip.
    :param direction: Pin direction. Valid values are 'in' and 'out'.
    """
    chip:int
    pin:int
    direction:str = "out"

    def init(self) -> GPIO:
        """
        Initializes periphery's GPIO.

        :returns: GPIO type from periphery.
        """
        try:
            return GPIO(f"/dev/gpiochip{self.chip}", self.pin, self.direction)
        except Exception as e:
            raise e
            # Use pass instead of raise when running sphinx
            #pass