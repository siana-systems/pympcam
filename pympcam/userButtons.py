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
