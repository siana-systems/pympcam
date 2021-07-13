from pympcam import commons
import unittest
import platform
from subprocess import check_output

class TestCommonsMethods(unittest.TestCase):
    def setUp(self) -> None:
        return

    def test_isMPCamBoard(self):
        if 'Linux' == platform.system():
            try:
                host = check_output(['lsb_release', '-i']).decode().replace("Distributor ID:\t", "").strip()
            except FileNotFoundError:
                host = check_output(['uname', '-n']).decode().strip()
        else:
            host = "not-Linux"

        if 'mpcam' in host:
            self.assertTrue(commons.isMPCamBoard())
        else:
            self.assertFalse(commons.isMPCamBoard())

    

