import unittest

# Importamos el código a testear.
from pais import Pais
from resumen import Resumen

####################################################################

class TestPais(unittest.TestCase):

    def setUp(self):
        # Usa el archivo real ubicado en la misma carpeta
        self.pais = Pais("Aprender2023_curado.csv")

    def test_tamano(self):
        self.assertEqual(self.pais.tamano(), 583967)

    def test_provincias(self):
        self.assertIn("MZA", self.pais.provincias)
        self.assertIn("SFE", self.pais.provincias)

    def test_resumen_provincia(self):
        resumen = self.pais.resumen_provincia("MZA")
        self.assertIsInstance(resumen, Resumen)
        self.assertGreater(resumen.cantidad, 0)

    def test_estudiantes_en_intervalo(self):
        cantidad = self.pais.estudiantes_en_intervalo("mat", 400, 600, {"MZA", "SFE"})
        self.assertIsInstance(cantidad, int)
        self.assertGreaterEqual(cantidad, 0)

####################################################################

unittest.main()