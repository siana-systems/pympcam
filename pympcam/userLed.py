##
# @file       userLed.py
# @author     SIANA Systems
# @date       06/17/2021
# @copyright  The MIT License (MIT)
# @brief      PyMPCam User LED functions.
#
# -----------------------------------------------------------------------------
# MIT License
# 
# Copyright (c) 2021 SIANA Systems
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------

from pympcam.commons import MpcamGpio
from os import path
import logging

class UserLed:
    """
    Controls User LEDs on MPCam board.

    Avaible LEDs:

    - LED1: Blue
    - LED2: Red
    """
    _LED1_SYSFS = "heartbeat"
    _LED2_SYSFS = "error"
    _LED_SYSFS = "/sys/class/leds/{}/brightness"
    
    def __init__(self):
        """
        Init function will try to use periphery to access LED GPIO.
        If it fails (it should, LED are in use by the kernel as for v1.0) it
        will use SYSFS path to interact with the LED.
        """
        self.log = logging.getLogger(__name__)
        try:
            #: GPIO instance of LED1, Blue.
            self.LED1 = MpcamGpio(9, 2, "out").init() # PZ2, blue
        except:
            self.log.info("Using sysfs for LED1")
            self.LED1 = self._LED_SYSFS.format(self._LED1_SYSFS)
        try:
            #: GPIO instance of LED2, Red.
            self.LED2 = MpcamGpio(7, 13, "out").init() # PH13, yellow
        except:
            self.log.info("Using sysfs for LED2")
            self.LED2 = self._LED_SYSFS.format(self._LED2_SYSFS)

    def turnOn(self, label:str=None) -> None:
        """
        Turns on user LEDs.

        :param label: LED to be turn on (LED1, LED2) or empty for all.
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

        :param label: LED to be turn off (LED1, LED2) or empty for all.
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
        
        :param label: LED to get state (LED1, LED2).
        :returns: True if LED is on.
        """
        led = self._get_led(label)
        if type(led) == str:
            with open(led, 'r') as f:
                return "1" == f.read(1)
        else:
            return led.read()

    def enableHeartbeat(self) -> bool:
        """
        Enable heartbeat trigger for user LED1.

        :returns: True if enabled.
        """
        return self._set_led_trigger(self._get_led("led1"), "heartbeat")

    def disableHeartbeat(self) -> bool:
        """
        Disable heartbeat trigger for user LED1.
        
        :returns: True if disabled.
        """
        return self._set_led_trigger(self._get_led("led1"), "none")
        

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

    def _set_led_trigger(self, led:str, trigger:str):
        if path.exists(led):
            try:
                with open(led.replace('brightness', 'trigger'), 'w') as f:
                    f.write(trigger)
                return True
            except Exception as e:
                self.log.warning(f"Error setting trigger {trigger} for {led}: \n{str(e)}")
                raise e
        else:
            raise Exception("LED is not in SYSFS")
        
