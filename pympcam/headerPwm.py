##
# @file       headerPwm.py
# @author     SIANA Systems
# @date       06/17/2021
# @copyright  The MIT License (MIT)
# @brief      PyMPCam Header PWM functions.
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

from periphery import PWM
import logging

class HeaderPwm:
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.PWM1 = PWM(0, 1) # PA5
        self.PWM2 = PWM(4, 3) # PD14

    def set(self, label:str, duty_cycle=.5, frequency=1):
        """
        Sets specified PWM to start.
        Warning: Duty cycle and frequency paramaters should 
        make sense with timer.

        :warning: Some combinations of duty_cycle and frequency may cause errors.

        :param label: PWM to be used (pwm1, pwm2).
        :param duty_cycle: Duty cycle for the PWM, as % between 0 and 1.
        :param frequency: Frequency for the PWM, as Hz.
        """
        pwm = self._get_pwm(label)
        pwm.frequency = frequency
        pwm.duty_cycle = duty_cycle
        pwm.enable()

    def get(self, label:str):
        """
        Gets PWM parameters.

        :param label: PWM to be get (pwm1, pwm2).
        :returns: Tuple with duty cycle and frequency.
        """
        pwm = self._get_pwm(label)
        return pwm.duty_cycle, pwm.frequency

    def close(self, label:str):
        """
        Closes a PWM device.

        :param label: PWM to be closed (pwm1, pwm2).
        """
        pwm = self._get_pwm(label)
        pwm.close()
    
    def _get_pwm(self, label:str) -> PWM:
        if label.lower() == "pwm1":
            return self.PWM1
        elif label.lower() == "pwm2":
            return self.PWM2
        else:
            raise Exception("Unkown user PWM label: {}".format(label))
