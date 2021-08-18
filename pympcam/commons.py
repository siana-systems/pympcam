##
# @file       commons.py
# @author     SIANA Systems
# @date       06/17/2021
# @copyright  The MIT License (MIT)
# @brief      PyMPCam Common functions.
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

import platform
from subprocess import check_output
from dataclasses import dataclass

def isMPCamBoard() -> bool:
    """
    Detects if library is running on MPCam board.
    
    :return: True if Running on MPCam board.
    """
    if 'Linux' == platform.system():
        try:
            if 'mpcam' in check_output(['lsb_release', '-i']).decode().replace("Distributor ID:\t", "").strip():
                return True

        except FileNotFoundError:
            # lsb_release is not installed => use uname
            if 'mpcam' in check_output(['uname','-n']).decode().strip():
                return True

        except Exception as e:
            raise e

    return False

# Periphery import
if isMPCamBoard():
    from periphery import GPIO
else:
    from pympcam.fakePeriphery import GPIO
    

@dataclass
class MpcamGpio:
    """
    Data class for MPCam GPIO.

    :todo: Verify which periphery version has `inverted gpio <https://python-periphery.readthedocs.io/en/latest/gpio.html>`_

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
