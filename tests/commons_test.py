from pympcam import commons
import unittest
from subprocess import check_output

class TestCommonsMethods(unittest.TestCase):
    def setUp(self) -> None:
        return

    def test_isMPCamBoard(self):
        cmd = check_output(['lsb_release', '-i']).decode().replace("Distributor ID:\t", "").strip()
        if cmd == 'mpcam':
            self.assertTrue(commons.isMPCamBoard())
        else:
            self.assertFalse(commons.isMPCamBoard())

    

