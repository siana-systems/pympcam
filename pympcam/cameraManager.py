##
# @file       cameraManager.py
# @author     SIANA Systems
# @date       07/2021
# @copyright  The MIT License (MIT)
# @brief      PyMPCam camera control functions.
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

import subprocess
from .commons import isMPCamBoard

import logging
from enum import IntEnum

class ExposureMode(IntEnum):
    """Supported camera auto-exposure modes.
    """
    AUTO = 0
    MANUAL = 1

class LineFreq(IntEnum):
    """Supported camera filters for power-line frequency.
    """
    DISABLED = 0
    F50Hz = 1
    F60Hz = 2
    AUTO = 3

class TestPattern(IntEnum):
    """Supported camera test patterns.
    """
    DISABLED = 0
    COLOR_BARS = 1
    COLOR_BARS_WITH_ROLLING_BARS = 2
    COLOR_SQUARES = 3
    COLOR_SQUARES_WITH_ROLLING_BARS = 4 

class CameraManager:
    """
    Controls the MPCam camerta.

    Note: other controls are available from OpenCV.
    """
    
    def __init__(self):
        self.log = logging.getLogger(__name__)
        self.is_mpcamHost = isMPCamBoard()

    @staticmethod
    def set_param(param, val):
        parm_val = "{}={}".format(param, val)
        subprocess.run(['v4l2-ctl','--set-ctrl',parm_val])

    @staticmethod
    def get_param(param):
        ret = subprocess.check_output(['v4l2-ctl','--get-ctrl',param]).decode().strip().split(':')
        return ret[0], ret[1]

    def flip_horizontal(self, enable: bool):
        """Flips the image around the horizontal.

            Args:
                enable: True if image should be flipped.
        """
        if self.is_mpcamHost:
            self.log.info("camera flip horizontal = {}".format(enable))
            CameraManager.set_param('horizontal_flip', 1 if enable else 0)

    def flip_vertical(self, enable: bool):
        """Flips the image around the vertical.

            Args:
                enable: True if image should be flipped.
        """
        if self.is_mpcamHost:
            self.log.info("camera flip vertical = {}".format(enable))
            CameraManager.set_param('vertical_flip', 1 if enable else 0)

    def set_autoGain(self, enable: bool):
        """Enable/Disable the camera auto-gain.

            Args:
                enable: True to enable auto-gain. False to disable it.
        """
        if self.is_mpcamHost:
            self.log.info("camera auto-gain = {}".format(enable))
            CameraManager.set_param('gain_automatic', 1 if enable else 0)

    def get_autoGain(self) -> bool:
        """Returns the camera auto-gain setting.

            Returns: True if auto-gain is set, or False if not.
        """
        if self.is_mpcamHost:
            param, val = CameraManager.get_param('gain_automatic')
            return bool(int(val)) if param == 'gain_automatic' else None

    def set_gainLevel(self, level: int):
        """Sets the camera gain level when auto-gain is disabled.
        
            Args:
                level: gain value between 0..1023
        """
        if self.is_mpcamHost:
            if level < 0 or level > 1023: raise ValueError
            self.log.info("camera gain level = {}".format(level))            
            CameraManager.set_param('gain', level)

    def get_gainLevel(self) -> int:
        """Returns the camera gain level."""
        if self.is_mpcamHost:
            param, val = CameraManager.get_param('gain')
            return int(val) if param == 'gain' else None           

    def set_autoExposure(self, mode: ExposureMode):
        """Sets the camera auto-exposure mode.

            Args:
                mode(ExposureMode): AUTO or MANUAL.
        """
        if self.is_mpcamHost:
            self.log.info("camera auto-exposure = {}".format(mode))
            CameraManager.set_param('auto_exposure', int(mode))

    def get_autoExposure(self) -> ExposureMode:
        """Returns the camera auto-exposure setting.

            Returns: MANUAL or AUTO.
        """
        if self.is_mpcamHost:
            param, val = CameraManager.get_param('auto_exposure')
            return ExposureMode(int(val)) if param == 'auto_exposure' else None

    def set_exposureLevel(self, level: int):
        """Sets the camera exposure level when auto-exposure is set to MANUAL.
        
            Args:
                level: expsoure value between 0..65535
        """
        if self.is_mpcamHost:
            if level < 0 or level > 65535: raise ValueError
            self.log.info("camera exposure level = {}".format(level))
            CameraManager.set_param('exposure', level)

    def get_exposureLevel(self) -> int:
        """Returns the camera exposure level."""
        if self.is_mpcamHost:
            param, val = CameraManager.get_param('exposure')
            return int(val) if param == 'exposure' else None 

    def set_powerLineFreq(self, freq: LineFreq):
        """Sets the camera power-line frequency.
        
            Args:
                freq(LineFreq): power-line frequency, either: DISABLED, F50Hz, F60Hz, AUTO
        """
        if self.is_mpcamHost:
            self.log.info("camera power-line freq = {}".format(freq))
            CameraManager.set_param('power_line_frequency', int(freq))

    def set_testPattern(self, pattern: TestPattern):
        """Sets the camera output test patterns.

            Args:
                pattern(TestPattern): the selected test pattern.
        """
        if self.is_mpcamHost:
            self.log.info("camera test pattern = {}".format(pattern))
            CameraManager.set_param('test_pattern', int(pattern))