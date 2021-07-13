import unittest

import random

from pympcam.cameraManager import CameraManager, ExposureMode

class TestCoralManagerMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.camera = CameraManager()
        return super().setUp()

    def teadDown(self) -> None:
        # restore camera settings
        self.camera.set_autogain(True)
        self.camera.set_autoExposure(ExposureMode.AUTO)
        return super().tearDown()

    def test_toggleAutoGain(self):
        # read auto-gain
        autoGain = self.camera.get_autoGain()
        # toggle auto-gain
        test_autoGain = False if autoGain else True
        # set new auto-gain
        self.camera.set_autoGain( test_autoGain )
        # read it back...
        toggled_autoGain = self.camera.get_autoGain()
        # validate...
        self.assertNotEqual(autoGain, toggled_autoGain)

    def test_withSetGainLevel_shouldGetSameGainLevel(self):
        # disable auto-gain
        self.camera.set_autoGain(False)
        # set test gain
        set_gain = random.randint(0,1023)
        self.camera.set_gainLevel( set_gain )
        # read it back...
        test_gain = self.camera.get_gainLevel()
        # validate...
        self.assertEqual(test_gain, set_gain)        

    def test_toggleAutoExposure(self):
        # read auto-exposure
        autoExposure = self.camera.get_autoExposure()
        # toggle auto-exposure
        test_autoExposure = ExposureMode.AUTO if autoExposure == ExposureMode.MANUAL else ExposureMode.AUTO
        # set new auto-exposure
        self.camera.set_autoExposure( test_autoExposure )
        # read it back...
        toggled_autoExpsore = self.camera.get_autoExposure()
        # validate...
        self.assertNotEqual(autoExposure, toggled_autoExpsore)

    def test_withSetExposureLevel_shouldGetSameExposureLevel(self):
        # disable auto-exposure
        self.camera.set_autoExposure(ExposureMode.MANUAL)
        # set test exposure
        set_exposure = random.randint(0,65535)
        self.camera.set_exposureLevel( set_exposure )
        # read it back...
        test_exposure = self.camera.get_exposureLevel()
        # validate...
        self.assertEqual(test_exposure, set_exposure) 
