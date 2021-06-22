from pympcam.commons import MpcamGpio
import logging

class UserLed:
    LED1 = MpcamGpio(9, 2, "out") # PZ2, blue
    LED2 = MpcamGpio(7, 13, "out") # PH13, yellow
    LED1_SYSFS = "heartbeat"
    LED2_SYSFS = "error"
    LED_SYSFS = "/sys/class/leds/{}/brightness"
    
    def __init__(self):
        """
        Init function will try to use periphery to access LED GPIO.
        If it fails (it should, LED are in use by the kernel as for v99.13) it
        will use SYSFS path to interact with the LED.
        """
        self.log = logging.getLogger(__name__)
        try:
            self.LED1.init()
        except:
            self.LED1 = self.LED_SYSFS.format(self.LED1_SYSFS)
        try:
            self.LED2.init()
        except:
            self.LED2 = self.LED_SYSFS.format(self.LED2_SYSFS)

    def turnOn(self, label:str=None) -> None:
        """
        Turns on user LEDs.

        :param label: LED to be turn on (led1, led2) or empty for all.
        """
        for led in self._get_leds(label):
            if type(led) == str:
                with open(led, 'w') as f:
                    f.write("1")
            else:
                led.write(True)


    def turnOff(self, label:str=None) -> None:
        """
        Turns off user LEDs.

        :param label: LED to be turn off (led1, led2) or empty for all.
        """
        for led in self._get_leds(label):
            if type(led) == str:
                with open(led, 'w') as f:
                    f.write("0")
            else:
                led.write(False)

    def getState(self, label:str=None) -> bool:
        """
        Gets current state of a user LED.
        
        :param label: LED to get state (led1, led2).
        :returns: True if LED is on.
        """
        led = self._get_led(label)
        if type(led) == str:
            with open(led, 'r') as f:
                return "1" == f.read(1)
        else:
            return led.read()

    def _get_leds(self, label:str) -> list:
        if label == None:
            return [self.LED1, self.LED2]
        if label.lower() == "led1":
            return [self.LED1]
        elif label.lower() == "led2":
            return [self.LED2]
        else:
            raise Exception("Unkown user LED label: {}".format(label))
    
    def _get_led(self, label:str):
        if label.lower() == "led1":
            return self.LED1
        elif label.lower() == "led2":
            return self.LED2
        else:
            raise Exception("Unkown user LED label: {}".format(label))
