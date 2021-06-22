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
