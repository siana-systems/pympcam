import unittest

import random

from pympcam.cameraManager import CameraManager, ExposureMode

class TestCoralManagerMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.camera = CameraManager()
        return super().setUp()

#--: GAIN :--------------------------------------------------------------------  

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

#--:EXPOSURE :-----------------------------------------------------------------

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

#--: WHITE-BALANCE :-----------------------------------------------------------

    def test_toggleAutoWhiteBalance(self):
        # read auto-WB
        autoWB = self.camera.get_autoWhiteBalance()
        # toggle auto-WB
        test_autoWB = False if autoWB else True
        # set new auto-WB
        self.camera.set_autoWhiteBalance( test_autoWB )
        # read it back...
        toggled_autoWB = self.camera.get_autoWhiteBalance()
        # validate...
        self.assertNotEqual(autoWB, toggled_autoWB)

    def test_withSetRedLevel_shouldGetSameRedLevel(self):
        # disable auto-WB
        self.camera.set_autoWhiteBalance(False)
        # set test red level
        set_red = random.randint(0,4095)
        self.camera.set_redBalanceLevel( set_red )
        # read it back...
        test_red = self.camera.get_redBalanceLevel()
        # validate...
        self.assertEqual(test_red, set_red) 

    def test_withSetBlueLevel_shouldGetSameBlueLevel(self):
        # disable auto-WB
        self.camera.set_autoWhiteBalance(False)
        # set test blue level
        set_blue = random.randint(0,4095)
        self.camera.set_blueBalanceLevel( set_blue )
        # read it back...
        test_blue = self.camera.get_blueBalanceLevel()
        # validate...
        self.assertEqual(test_blue, set_blue) 