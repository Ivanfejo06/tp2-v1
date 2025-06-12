import unittest

# Importamos el código a testear.
from resumen import Resumen

####################################################################

class TestResumen(unittest.TestCase):

    def test_repr(self):
        r = Resumen(30478, 517.04, 536.54, 0.54, 0.00, 0.51)
        esperado = "<Mat:517.04, Len:536.54, NSE:0.54, Rural:0.00, Estado:0.51, N:30478>"
        self.assertEqual(str(r), esperado)

    def test_eq_true(self):
        r1 = Resumen(1000, 500.123, 505.321, 0.1234, 0.05, 0.95)
        r2 = Resumen(1000, 500.1225, 505.3211, 0.1235, 0.0501, 0.9500)
        self.assertTrue(r1 == r2)

    def test_eq_false(self):
        r1 = Resumen(100, 500, 500, 0.1, 0.5, 0.5)
        r2 = Resumen(100, 501, 500, 0.1, 0.5, 0.5)
        self.assertFalse(r1 == r2)

####################################################################

unittest.main()
