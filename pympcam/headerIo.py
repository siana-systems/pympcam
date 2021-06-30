##
# @file       headerIo.py
# @author     SIANA Systems
# @date       06/17/2021
# @copyright  The MIT License (MIT)
# @brief      PyMPCam Header IO functions.
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
from periphery import GPIO
import logging

class HeadersIo:
    """
    Controls Headers Input/Output on MPCam board.
    """

    GPIO1_IS_PWM = True

    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.GPIO0:GPIO = MpcamGpio(3, 9, "out").init() # PD9
        if not self.GPIO1_IS_PWM:
            self.GPIO1 = MpcamGpio(3, 14, "out").init() # PD14
        self.GPIO2:GPIO = MpcamGpio(9, 6, "out").init() # PZ6
        self.GPIO3:GPIO = MpcamGpio(9, 7, "out").init() # PZ7

    def get(self, label:str) -> int:
        """
        Gets GPIO current state.

        :param label: Header DIO to get (do0, do1, do2, do3).
        :returns: DIO current state: 1 if active, 0 if not.
        """
        dio = self._get_dio(label)
        state = dio.read()
        self.log.debug(f"{label} value is {state}")
        return int(state)

    def set(self, label:str, value:bool=None) -> int:
        """
        Sets (or toggles) GPIO current state. If value is provided,
        is set as current.
        
        :param label: Header DIO to get (do0, do1, do2, do3).
        :param value: Forces a state to selected DIO.
        :returns: DIO current state: 1 if active, 0 if not.
        """
        dio = self._get_dio(label)
        if value is None:
            dio.write(not dio.read())
        else:
            dio.write(value)
        state = dio.read()
        self.log.debug(f"{label} value is {state}")
        return int(state)

    def _get_dio(self, label:str) -> GPIO:
        if label.lower() == "do0":
            return self.GPIO0
        elif (label.lower() == "do1") and (not self.GPIO1_IS_PWM):
             return self.GPIO1
        elif label.lower() == "do2":
            return self.GPIO2
        elif label.lower() == "do3":
            return self.GPIO3
        else:
            raise Exception("Uknown user GPIO label: {}".format(label))
