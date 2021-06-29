##
# @file       userButtons.py
# @author     SIANA Systems
# @date       06/17/2021
# @copyright  The MIT License (MIT)
# @brief      PyMPCam User Buttons functions.
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

from periphery.gpio import GPIO
from pympcam.commons import MpcamGpio
import logging

class UserButtons:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.SW1:GPIO = MpcamGpio(7, 9, "in").init() # PH9
        self.SW2:GPIO = MpcamGpio(8, 1, "in").init() # PI1

    def getState(self, button:str=None):
        """
        Gets current button state.

        :param button: button to get state.
        :returns: True if button was pressed.
        """
        state = []
        for btn in self._get_buttons(button):
            state.append(not btn.read())
        if len(state) == 1:
            return state[0]
        else:
            return state

    def pollState(self, button:GPIO, timeoutSeconds=10) -> bool:
        """
        Polls button state during a period of time (timeout).
        Button change is detected either by faling or raising edge.
        
        :param button: button to get state.
        :param timeoutSeconds: time to wait for button state change, in seconds.
        :returns: True if button was pressed.
        """
        button.edge = "both"
        state = button.poll(timeoutSeconds)
        self.log.debug(f"Button poll {state}")
        button.edge = "none"
        return state

    def _get_buttons(self, label:str) -> list:
        if label == None:
            return [self.SW1, self.SW2]
        if label.lower() == "sw1":
            return [self.SW1]
        elif label.lower() == "sw2":
            return [self.SW2]
        else:
            raise Exception("Unknown user button label: {}".format(label))
