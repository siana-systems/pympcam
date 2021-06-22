import unittest

from pympcam.headerIo import HeadersIo

class TestHeaderIoMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.dio = HeadersIo()
        dios = ["do0", "do2", "do3"]
        if not self.dio.GPIO1_IS_PWM:
            dios.append("dio1")
        for dio in dios:
            self.dio.set(dio, value=False)
        return super().setUp()

    def test_dio0_get(self):
        self.assertEqual(0, self.dio.get("do0"))
    
    def test_dio0_set(self):
        self.dio.set("do0")
        self.assertEqual(1, self.dio.get("do0"))

    def test_dio0_set_disable(self):
        self.dio.set("do0", value=False)
        self.assertEqual(0, self.dio.get("do0"))
    
    def test_dio0_set_enable(self):
        self.dio.set("do0", value=True)
        self.assertEqual(1, self.dio.get("do0"))
    
    @unittest.skipIf(HeadersIo.GPIO1_IS_PWM, "GPIO1 is PWM")
    def test_dio1_get(self):
        self.assertEqual(0, self.dio.get("do1"))
    
    @unittest.skipIf(HeadersIo.GPIO1_IS_PWM, "GPIO1 is PWM")
    def test_dio1_set(self):
        self.dio.set("do1")
        self.assertEqual(1, self.dio.get("do1"))

    @unittest.skipIf(HeadersIo.GPIO1_IS_PWM, "GPIO1 is PWM")
    def test_dio1_set_disable(self):
        self.dio.set("do1", value=False)
        self.assertEqual(0, self.dio.get("do1"))
    
    @unittest.skipIf(HeadersIo.GPIO1_IS_PWM, "GPIO1 is PWM")
    def test_dio1_set_enable(self):
        self.dio.set("do1", value=True)
        self.assertEqual(1, self.dio.get("do1"))
    
    def test_dio2_get(self):
        self.assertEqual(0, self.dio.get("do2"))
    
    def test_dio2_set(self):
        self.dio.set("do2")
        self.assertEqual(1, self.dio.get("do2"))

    def test_dio2_set_disable(self):
        self.dio.set("do2", value=False)
        self.assertEqual(0, self.dio.get("do2"))
    
    def test_dio2_set_enable(self):
        self.dio.set("do2", value=True)
        self.assertEqual(1, self.dio.get("do2"))
    
    def test_dio3_get(self):
        self.assertEqual(0, self.dio.get("do3"))
    
    def test_dio3_set(self):
        self.dio.set("do3")
        self.assertEqual(1, self.dio.get("do3"))

    def test_dio3_set_disable(self):
        self.dio.set("do3", value=False)
        self.assertEqual(0, self.dio.get("do3"))
    
    def test_dio3_set_enable(self):
        self.dio.set("do3", value=True)
        self.assertEqual(1, self.dio.get("do3"))

    def test_diox_get(self):
        with self.assertRaises(Exception):
            self.dio.get("dox")
    
    def test_diox_set(self):
        with self.assertRaises(Exception):
            self.dio.set("dox")
