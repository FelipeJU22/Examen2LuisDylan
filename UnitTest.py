import unittest
from Examen2 import MiClase

class TestMiClase(unittest.TestCase):

    def setUp(self):
        self.mi_clase_obj = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

    def test_ObtieneValencia(self):
        self.assertEqual(self.mi_clase_obj.ObtieneValencia(1234567), 4)

    def test_DivisibleTempo(self):
        self.assertEqual(self.mi_clase_obj.DivisibleTempo(10), [1, 2, 5, 10])

    def test_ObtieneMasBailable(self):
        self.assertEqual(self.mi_clase_obj.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)

    def test_VerificaListaCanciones(self):
        self.assertTrue(self.mi_clase_obj.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]))

if __name__ == '__main__':
    unittest.main()
