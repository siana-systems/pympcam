##
# @file       fakePeriphery.py
# @author     SIANA Systems
# @date       07/05/2021
# @copyright  The MIT License (MIT)
# @brief      PyMPCam Fake Periphery functions.
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

import sys, select
import logging

class GPIO:
    """
    Data class for fake GPIO.

    :param chip: Chip number for the GPIO.
    :param pin: Pin number for the GPIO chip.
    :param direction: Pin direction. Valid values are 'in' and 'out'.
    """
    chip:int
    pin:int
    direction:str = 'out'
    edge:str = 'both'
    FakeValue:bool = False

    def __init__(self, chip:int, pin:int, direction:str='out') -> None:
        self.chip = chip
        self.pin = pin
        self.direction = direction
        self.log = logging.getLogger(__name__)
        self.log.warning(f"Init Fake Periphery GPIO {self.chip}:{self.pin}")

    def write(self, value:bool):
        self.FakeValue = value
        self.log.info(f"Write Fake Periphery GPIO {self.chip}:{self.pin} = {self.FakeValue}")
        return True
    
    def read(self):
        self.log.info(f"Read Fake Periphery GPIO {self.chip}:{self.pin} = {self.FakeValue}")
        if self.direction == 'in':
            return not self.FakeValue
        return self.FakeValue

    def poll(self, timeout:float):
        self.log.info(f"Poll Fake Periphery GPIO {self.chip}:{self.pin}")
        i, o, e = select.select([sys.stdin], [], [], timeout)
        return i


class PWM:
    """
    Data class for fake PWM.

    :param chip: Chip number for the GPIO.
    :param pin: Pin number for the GPIO chip.
    """
    duty_cycle:float
    frequency:int

    def __init__(self, chip:int, pin:int) -> None:
        self.chip = chip
        self.pin = pin
        self.log = logging.getLogger(__name__)
        self.log.warning(f"Init Fake Periphery PWM {self.chip}:{self.pin}")

    def enable(self):
        self.log.info(f"Enable Fake Periphery PWM {self.chip}:{self.pin}")
        return True

    def close(self):
        self.log.info(f"Close Fake Periphery PWM {self.chip}:{self.pin}")
        return True
