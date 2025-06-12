import unittest

# Importamos el código a testear.
from estudiante import Estudiante

####################################################################

class TestEstudiante(unittest.TestCase):

    def test_repr(self):
        e = Estudiante("MZA", 466.76, 550.32, 0.01, "urbano", "estatal")
        esperado = "<Mat:466.76, Len:550.32, NSE:0.01, Urbano, Estatal, MZA>"
        self.assertEqual(str(e), esperado)

    def test_eq_true(self):
        e1 = Estudiante("MIS", 507.25, 488.68, -0.26, "rural", "privado")
        e2 = Estudiante("MIS", 507.251, 488.681, -0.2599, "rural", "privado")
        self.assertTrue(e1 == e2)

    def test_eq_false(self):
        e1 = Estudiante("SFE", 500, 500, 0.5, "urbano", "estatal")
        e2 = Estudiante("SFE", 501, 500, 0.5, "urbano", "estatal")
        self.assertFalse(e1 == e2)

####################################################################

unittest.main()
